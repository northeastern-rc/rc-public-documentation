# Documentation Primer

## Purpose

:::{important}
Remember that this style guide is a reference for team members working on documentation. It is essential to keep it up-to-date and easily accessible for all contributors.
:::

This style guide outlines the best practices and conventions for creating clear, consistent, high-quality documentation for our project. By following these guidelines, we can ensure a cohesive writing style and tone across all documentation.

This style guide provides guidelines for writing clear, concise, and consistent documentation. It covers language, tone, formatting, and other aspects of documentation.

##  Writing Style
The writing style in documentation is critical for ensuring consistency and understanding. Here are some best practices:

**Clarity**: Be as clear and straightforward as possible. Avoid ambiguity. Documentation is not a place for complex sentences and unusual words.

:::{list-table}
:header-rows: 1
* - ❌ Do Not
  - ✅ Do
* - The initiation of the replication process...
  - To start the replication process...
:::

**Conciseness**: Keep sentences and paragraphs short. This makes text easier to read and understand.

:::{list-table}
:header-rows: 1
* - ❌ Do Not
  - ✅ Do
* - Once the process has been completed successfully, the next step is...
  - After completing the process, next...
:::

**Active Voice**: Use the active voice whenever possible as it is more straightforward and engaging.

:::{list-table}
:header-rows: 1
* - ❌ Do Not
  - ✅ Do
* - The command can be executed by the user.
  - The user can execute the command.
:::

**Address the Reader**: Use the second person ("you") to address the reader directly.

:::{list-table}
:header-rows: 1

* - ❌ Do Not
  - ✅ Do
* - One can see the results by... <br>
  - You can see the results by...<br>
:::

- Avoid using jargon and slang, as they can be confusing.
- Keep your writing easy to read by using short sentences and paragraphs.
- If you need to explain complex concepts, break them into smaller, more manageable sections to help your reader understand your message.

##  Formatting
MyST allows for markdown to be used for our Spinx project (i.e., RTD).

:::{admonition} Bookmark and Review-worth Reference
Check out this [Markdown cheatsheet].
:::


Commonly used elements follow the [MyST-Typography].

Directives allow us to insert and format various elements (e.g., images, callouts, etc.). We use `colon_fence` to replace the typical hyphens Learn more about  [Colon Fence].

:::::{important}
We use the `colon_fence` extension the markdown rendered by Myst parses three colons (i.e., *:*) to open and close blocks. ([about colon_fence]).

::::{note}
[Myst-Parser Documentation] includes several constructs we can use to enhance our pages. **Use elements with purpose, whether to call attention, reference related content, or warn.
::::

Nesting blocks, along with the ability set parameters inline.

::::{note}
There is no need to indent source text, as nested directives are explicitly clear by the number of `:` characters are used to open and close.
::::

::::{attention}

**Do not add line-breaks unless a line break in the rendered view is to need a line break.** Each paragraph remains on the same line, with line-breaks using to clearly show transitions between paragraphs, sections, and directives.

:::{tip}
Set *Soft-Wrap* to be set to 100 characters by default when viewing `*.md`

<figure>
  <img src="../_static/image/settings-softwrap.png" alt="Soft-Wrap Setting" style="width:100%">
  <figcaption>Fig. Soft-Wrap set to 100 characters in PyCharm's <i>General</i> settings.</figcaption>
</figure>
:::

:::{note}
Add line-breaks before and after the opening and closing of directives (i.e., outside the struct). Only add a single line-break after opening, which is the case for most directives; for those that do not require any inputs but titles (e.g., `:::{directive} Title`), omit line-breaks after the opening.
:::

::::

::::{important}
These nested admonitions were done, mostly, to demonstrate how it can be done. There are exceptions, but this is quite nested: be sure to consider if the flow of information is done most effectively when nests deeper, or even as as deep as this example (i.e., five colons `:::::` deep).
::::

:::::

Consistent formatting makes your documentation look professional and easy to read. Use consistent formatting for headings, lists, tables, and other elements, and adequately nest subheadings and lists. Here are some guidelines:

- **Headings**: Use headings and subheadings to structure your content. In MyST, use # for level 1 headings, ## for level 2, and so on.
- **Lists:** Use bulleted lists for unordered items and numbered lists for ordered items. In MyST, use or  for unordered lists and 1. for ordered lists.
- **Bold and Italics**: Use bold to highlight important concepts and italics to indicate new terms. In MyST, use bold text** for bold and italic text* for italics.
- **Code Blocks**: Use code blocks to present code snippets. In MyST, use triple backticks to create code blocks and specify the language for syntax highlighting.
- **Admonitions**: Use MyST syntax to create admonitions highlighting notes, tips, warnings, and other important information. For example, use `:::{note}` or `:::{warning}` to create admonitions.

##  Code Example
Code examples can help readers understand how to use a feature or solve a problem. Here are some guidelines to follow:
- **Clarity**: Ensure that your code is easy to understand. Include comments to explain complex or essential parts of the code.
- **Syntax** Highlighting: Use syntax highlighting to make your code easier to read. In MyST, you can specify the language for syntax highlighting in code blocks (see [Myst Source code and APIs]).
- **Error Handling**: If relevant, show how to handle errors and exceptions.
- **Consistency**: Ensure your code examples follow the same coding style, including indentation and naming conventions.
- **GitHub**: Reference the repo if snippets from another RC GitHub project is referred.

##  Language and Terminology
Clear and consistent language and terminology are crucial for effective communication. Here are some guidelines:
- **Consistency**: Use terminology consistently. Don't use different terms for the same concept.
- **Acronyms**: Always define acronyms the first time you use them.
- **Jargon**: Avoid using jargon unless necessary. If you have to use it, define it first.
- **Language**: Use either American or British English consistently throughout your documentation.
