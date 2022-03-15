# Contributing to Discord Warsim
## Code Comments
No multi-line comments, especially not for singlar lines. \
Use `TODO:` to mark TODOs in code. \
Use `FIXME:` or `TODO:` to mark TODOs about bugs or other issues. \
Use three #'s for each comment. (optional)
## New Features/Ideas
When proposing new features and ideas, open up an issue for the idea, unless you already have code prepared.
If you have code prepared than open up a pull request and move forward from there.
## Major modifications to existing features
### What do you mean by 'Major modifications to existing features'?
Major modifications to existing features means adding substantial new functions and methods, anything that would cause large changes elsewhere, or cause issues to existing users. \
 \
For example, a new, more efficient method of saving user data or config data would be a major modification to an existing feature.
### Modifications that would cause issues for existing users
When creating modifications like new config formats, save formats, etc. create a tool to adapt existing data. Or do it manually.
### New functions, methods, and commands
Always always always add some for of documentation or obvious meaning or use for it. 
Give an example use, documentation, explanitory name, etc.
### Changes outside of the primarily effected feature
If the changes effect external features update the feature or document the change.
## Bugfixes
Bugfixes are simple, remove `TODO:` or `FIXME:` about the bug, and test before commiting.
## Additions to unfinished code
Additions to unfinished code are like bugfixes, remove `TODO:` about what you did, and open a pull request.