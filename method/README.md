# METHOD OVERVIEW

This directory contains chat logs and other files that together document the method employed to obtain the final results. This documentation can be useful in a variety of ways, especially alongside LLMs.
For example, an LLM can injest these files and the user can query in depth about the thinking process/logic involved in order to improve or expand upon the project.
Or, a user can read through the documentation and query a model about any questions they have to help grasp unfamiliar concepts.
In this way, the systems thinking and engineering employed in building the project is one of the assets produced as a by-product, and hold similar value to the actual structured data this project attempts to produce.
Lastly, I believe this kind of documentation is worth saving for later analysis and training of LLM models or in building custom skills for agentic processes to use.

## Relative Methodology
### Stage-00 Planning

The methodology of the work-flow generally looks like this:
- query LLM with ideas about the project
- during initial chats try to define the end result as well as initial implementation ideas
- try to suggest or identify failure points
- offer context on the planned tech stack as well as personal area of expertise

During these initial chats the responses will help you identify assets for the project such as:
- programs
- languages
- organizations/services (data sources, 3rd parties offering useful web services, etc.)
- data manipulation techniques

Try to be recursive in your chat. By this I mean, ask meta-questions:
- ask for analysis on your own method so far, failure points? Better ways to accomplish a task?
- ask things like, how do others generally accomplish programmatic task X?
- Can you list the current tech stach for this project, do the technologies support each other and would some other combination work better?

By adding these kinds of questions during research, you can improve the engineering and approach as you build and learn more.

After these intial queries the chats should be reviewed to identify the information that will potentially be used in the project. Personally I try to do this on paper to reduce machine time and avoid further querying. Assets will need to be explored, visit a suggested data provider's site to learn about it from the source, read documentation on the tools and languages, etc.

Once the distinct pieces involved in the project are identified and properly researched, begin figuring out a basic implementation. For myself, I generally default to the most immediate next step, because often a project can change depending how each distinct piece actually succeeds or fails.

At this point if needed another chat can be used to help plan out the first immediate implementation piece, in the case of this repo that was acquiring the OpenStreetMap data and parsing it. Employ the same techniques used when planning the high-level overview. Record rough implementation sequence for this component.

### Stage-01 Implementation

This stage is when you move from information gathering to testing actual programmatic processes. If you are working with unfamiliar techniques/technologies utilize a chat to troubleshoot during this process.

*NOTE: The purpose of building in this way is not to employ agentic techiques to build something for you. If you do that you will most probably lose control (or at least full understanding) of the project. Be a part of the process, be a co-creator so you can own every step of the project, and therefore employ granular, intentional engineering.*

The way I like to think of this stage is this:
- inform the model of my expertise
- define the tech stack, hardware, OS and software
- try to imbue your engineering philosophies into your prompts e.g. "I want to build it in this way because..."
- be flexible, define your logic and ask for and accept well reasoned alternatives

Chat logs from this stage are typically structured in this way:
- I want to do this using these technologies, identify a sequence of implementation
- during step X of the posited implementation I got this standard error

Iterate through this as you work, document what works, what doesn't and why. Prompt the model to change the posited method if it conflicts with your logical understanding. Explain yourself, "you suggested to do X, I would rather do it in this way, here is why, what do you think is this solid logic?" I am the one running commands, I don't have to do what a model suggests. I try to avoid commanding language.

Never do a "one and done". Work in a virtual environment, verify the complete programmatic process you are attempting to build. Completely document it so that you can destroy your intial test environment and repeat it. Even if just doing something ephemeral/transient like obtaining info. Define it programatically, and prove it will work again.

