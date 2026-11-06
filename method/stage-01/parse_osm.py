import json
import csv

def parse_osm_geojson(input_file="buffalo_businesses.geojson", output_file="buffalo_business_leads.csv"):
    print(f"Loading {input_file}...")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {input_file}. Make sure you ran 'osmium export' first.")
        return

    features = data.get("features", [])
    print(f"Processing {len(features)} features...")

    rows = []
    for feature in features:
        props = feature.get("properties", {})
        geometry = feature.get("geometry", {})
        coords = geometry.get("coordinates", [None, None]) # [lon, lat] for GeoJSON
        
        # Extract location coordinates if it's a point (or center for polygons)
        longitude = coords[0] if len(coords) > 0 else None
        latitude = coords[1] if len(coords) > 1 else None

        # Determine the primary business category
        category = None
        for key in ["shop", "office", "amenity", "craft", "industrial"]:
            if key in props:
                category = f"{key}={props[key]}"
                break

        # Construct address components
        house_num = props.get("addr:housenumber", "")
        street = props.get("addr:street", "")
        city = props.get("addr:city", "Buffalo")
        postcode = props.get("addr:postcode", "")
        full_address = f"{house_num} {street}, {city} NY {postcode}".strip()
        if full_address == ", NY":
            full_address = ""

        # Gather contact details (checking both standard tags and contact: prefixed tags)
        phone = props.get("phone") or props.get("contact:phone", "")
        website = props.get("website") or props.get("contact:website", "")
        email = props.get("email") or props.get("contact:email", "")

        row = {
            "name": props.get("name", "Unknown / Unnamed"),
            "category": category,
            "address": full_address,
            "phone": phone,
            "website": website,
            "email": email,
            "latitude": latitude,
            "longitude": longitude,
            "osm_id": props.get("@id", "")
        }
        rows.append(row)

    # Define CSV columns
    fieldnames = ["name", "category", "address", "phone", "website", "email", "latitude", "longitude", "osm_id"]

    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"Successfully exported {len(rows)} records to {output_file}")

if __name__ == "__main__":
    parse_osm_geojson()
