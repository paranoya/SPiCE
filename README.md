# Self-consistent Photo-ionization and Chemical Evolution (SPiCE)

This is a git repository for our new chemical evolution code. I hope we can use to work together!

It contains several branches (e.g. `alfa`) that correspond to a previous attempt. Let us try to use `master` this time for the "production version". I'd advocate for creating "physical" branches, such as e.g. "dust" or "new yields", rather than "personal" branches with our names. Please see below for instructions.

## Basic git instructions

To clone the repository on your computer, 

`git clone https://github.com/paranoya/SPiCE/`

To keep up to date with the changes made by other people,

`git pull`

every now and then. When you feel ready to share your work with others,

`git add`
`git commit -m <short-but-descriptive-comment>`
`git push`

### Working with branches

Rather than working directly on the `master` branch, it may be safer to create your own:

`git branch <my-stuff>`

If you want to change between branches

`git checkout <nombre_de_la_rama>`

In order to watch all the branches you must checkout at least once to every branch.

Once the work on a given branch is complete and ready to be integrated into the `master` version:

`git merge <my-stuff>`

At some point, you'll want to delete the branch

`git branch -d <my-stuff>`

and start working on something else.

### Conflicts

Sooner or later, you will find a conflict while doing a pull. You can always write

`git reset --hard`

to go back to a previous version. But be careful! It overwrites your local files!

If you write

`git log [--oneline]`

You can come back to a concrete point of the historial with

`git reset --hard <numero SHA>`

Conflicts arise because a given file has been modified differently in two branches. The conflict (to be solved manually) is delimited by `<<<<<<<`, `=======`, and `>>>>>>>`. Write whatever you want to publish, remove the markers, do the usual `git add` to mark the conflict as solved, and try again.

Good luck!
