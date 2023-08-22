(best-practices-sw)=
# Best SW Practices
Good software practices are vital for successful scientific computing. This page outlines the best methods to follow when developing and running software on HPC systems.


## Coding Standards

Adhering to coding standards ensures your code is readable, maintainable, and less prone to errors.

- **Follow a Style Guide**: Include a style guide relevant to your programming language.
- **Use Meaningful Names**: Name variables and functions descriptively.
- **Comment Wisely**: Write comments that explain the 'why,' not the 'what.'

## Version Control

Utilizing a version control system like Git helps track changes, allows collaboration with others, and is essential for reproducibility.

- **Commit Regularly**: Make frequent, small commits.
- **Use Meaningful Commit Messages**: Describe what and why changes were made.
- **Keep a Changelog**: Document significant changes in a human-readable file.

## Documentation

Proper documentation helps others (and you in the future) understand your code.

- **Write inline comments**: Explain complex or non-intuitive parts of the code.
- **Maintain a README**: Include setup, usage, and other essential information.
- **Use automated documentation tools**: Tools like Doxygen or Sphinx can help.

## Testing

Implementing automated tests ensures that your code behaves as expected.

- **Write Unit Tests** on individual code units for correctness.
- **Perform Integration Tests** between different code parts.
- **Automate testing** using Continuous Integration tools to run tests automatically.

## Dependency Management

Managing dependencies effectively avoids conflicts and ensures reproducibility.

- **Use Dependency Management tools** like Conda or virtualenv.
- **Specify exact versions**: Note the specific versions of dependencies.

## Performance Considerations

Consider performance throughout the development process.

- **Profile often: Identify bottlenecks and areas for optimization.
- **Consider parallelization: Utilize parallel computing resources.

## Security

Please follow the best practices to keep your code and data secure.

- **Keep Sensitive Information Private**: Use environment variables for secrets.
- **Stay Updated**: Keep dependencies updated to avoid known vulnerabilities.

## Collaboration

Effective collaboration fosters quality and productivity.

- **Communicate Openly**: Keep lines of communication open with your team.
- **Use Collaboration Platforms**: GitHub or GitLab facilitate collaboration.

---

These best practices will help develop high-quality, maintainable, and performant software suitable for HPC and other computational environments. Please always seek feedback from peers, and don't hesitate to consult the HPC support team for specific guidance.
