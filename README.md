
# Research Computing Public Documentation

[![GitHub-CI][github-ci]][github-link]
[![Documentation Status][rtd-badge]][rtd-link]

This repository contains the source files for the Research Computing documentation.

HPC users can submit issues and bugs in the documentation [here](https://github.com/northeastern-rc/rc-public-documentation/issues/new/choose).

## Basic Development Workflow

Following are the basic steps for contributing to the RC documentation.

1. In the terminal, go to the folder where we want to clone the repo.

2. Use the following command:

```
git clone https://github.com/northeastern-rc/rc-public-documentation.git0
```

 This should result in an output similar to following:

```
Cloning into 'rc-public-documentation'...
remote: Enumerating objects: 9694, done.
remote: Counting objects: 100% (2891/2891), done.
remote: Compressing objects: 100% (733/733), done.
remote: Total 9694 (delta 2413), reused 2371 (delta 2158), pack-reused 6803
Receiving objects: 100% (9694/9694), 91.99 MiB | 10.76 MiB/s, done.
Resolving deltas: 100% (6479/6479), done.`
```

3. If we already have the documentation project on our computer, we run the following commands in the terminal.

```
git checkout master
git pull
```

This should bring the local copy of the project to the same state as the remote copy (master). We should get a message similar to the following

```
Already on 'master'
Your branch is up to date with 'origin/master'.
```

or

```
Already up to date.
```

4. Now, to do our work, we’ll create a new branch from master and switch to this new branch, using the following command:

```
git checkout -b new-branch-name
```

We can replace the `new-branch-name` with any appropriate name.

5. We can use the command `git branch` to check if we are on the branch that we just created, which we should be working on, which should result in the following, (with the `*` next to the name of the branch we are working on)

```
*new-branch-name
master
```

6. We can now make all the changes we want to make for the specific small task/edit we want to do.

7. Once done with the change, use the following commands to add and commit the changes, with a relevant commit message.

```
git add .
git commit -m “This is the commit message”`
```

(A commit message summarizes what the change is about. Notice the `.` at the end of `git add`, which tells to stage all the modified/new files.)

8. To preview documentation changes on our local machine, we can build and run the docker container ([instructions here](https://github.com/northeastern-rc/rc-public-documentation/blob/master/container/README.md)) and navigate to the corresponding page.

9. Now, the changes are ready to be pushed to remote. To push, use the following command:

```
git push
```

9. The above command should create a pull request (PR) on Github. Add reviewers to your PR for reviewing the changes. Once the review is complete someone can merge the PR, completing the process.

## Advanced Development

Clone repo:

```bash
git clone git@github.com:northeastern-rc/rc-public-documentation.git
```

Then, either open PyCharm and create python environment (some find easier to create environment using PyCharm):

<img src=".README_images/environment1.png" alt="env1" width="300"/>
<br>
<img src=".README_images/environment2.png" alt="env1" width="300"/>

OR, do so via the command-line:

```bash
cd rc-public-documentation

python3.11 -m venv .venv
source venv/bin/activate
pip install --upgrade pip
```

-----

Next, for those using Mac, install pre-commit via `brew`:

```bash
brew install pre-commit
```

For those on windows, use `pip`:

```bash
pip install pre-commit
```

Then, install `pre-commit` for RTD development:

```bash
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit

pip install -r docs/requirements.txt
```

---

[Install Dependencies][install-vscode]:

Launch VS-Code and open the project folder.

Install [myst-plugin-install][myst-plugin-install]; also, install directly from VS-Code by searching Extensions for `myst`.

![](.README_images/myst-plugin-screenshot.png)

You can use the [amazing markdown lint VS Code extension](https://thisdavej.com/build-an-amazing-markdown-editor-using-visual-studio-code-and-pandoc/#:~:text=markdownlint%20VS%20Code%20extension) developed by David Anson.  Here are the steps:

- Press `F1` to open the VS Code Command Palette.
- Type `ext install markdownlint` to find the extension
- Press Enter or click the cloud icon to install it
- Restart Visual Studio Code if prompted

Or for package development:

```bash
pip install myst-parser
npm install -g myst-cli
```

- Open Visual Studio Code
- Press `Ctrl+P`/`Ctrl+P`/`⌘P` to open the Quick Open dialog
- Type `ext install markdownlint` to find the extension
- Click the `Install` button, then the `Enable` button

You can also create a separate Window pane to preview your Markdown.  To do this:

- Press F1 to bring up the VS Code Command Palette.
- Type “mark” to narrow down the list of commands to “markdown” commands.
- Click “Markdown: Open Preview to the Side as shown here:
- Markdown Preview
![](.README_images/e3a69125.png)

## Additional

- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
- [Markdown helper](https://marketplace.visualstudio.com/items?itemName=joshbax.mdhelper)
- [emojisense](https://marketplace.visualstudio.com/items?itemName=bierner.emojisense)
- [markdown-all-in-one](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

<https://sphinx-design.readthedocs.io/en/latest/dropdowns.html>

## Contributing

We welcome all contributions!
See the [Contributing Guide](https://myst-parser.readthedocs.io/en/latest/develop/index.html) for more details.

[github-ci]: https://github.com/executablebooks/MyST-Parser/workflows/continuous-integration/badge.svg?branch=master
[github-link]: https://github.com/executablebooks/MyST-Parser
[rtd-badge]: https://readthedocs.org/projects/myst-parser/badge/?version=latest
[rtd-link]: https://myst-parser.readthedocs.io/en/latest/?badge=latest
[install-vscode]: https://code.visualstudio.com/
[myst-plugin-install]: https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight
