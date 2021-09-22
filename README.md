# Project Electron Website

The public website for Project Electron available at [https://projectelectron.rockarch.org/](https://projectelectron.rockarch.org/). This site is implemented as a [Jekyll](https://jekyllrb.com/) static site using the [Type Theme](https://github.com/rohanchandra/type-theme). Site contents is in the Markdown format and can be accessed in the `/contents` directory.

[![Build Status](https://travis-ci.com/RockefellerArchiveCenter/project_electron.svg?branch=gh-pages)](https://travis-ci.org/RockefellerArchiveCenter/project_electron)

## Getting Started
Install [git](https://git-scm.com/) and clone the repository:

    $ git clone https://github.com/RockefellerArchiveCenter/project_electron.git

With [Ruby](https://www.ruby-lang.org/en/documentation/installation/), [Bundler](https://bundler.io/), and [Jekyll](https://jekyllrb.com/) installed, you can view the site locally from the project's root.

Install dependencies:

    $ bundle install

Build the site locally:

    $ bundle exec jekyll serve

Once the application starts successfully, you should be able to access the application in your browser at `http://localhost:4000`.

## Usage
Use `bundle exec jekyll build` to build the initial Jekyll `_site` directory which can be served.

Run `bundle exec htmlproofer ./_site` to validate HTML output with [htmlproofer](https://github.com/gjtorikian/html-proofer).

## License

The Project Electron website is released under an [MIT License](LICENSE).

The Project Electron website content is released under a [CC0 License](LICENSE-CC0.md).
