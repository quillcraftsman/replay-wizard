# ReplayWizard

ReplayWizard is a powerful automation tool designed to streamline your workflow by capturing and replaying your 
interactions with your computer 

You can find **Full Project Documentation** [here][documentation_path]

![ReplayWizard logo](https://github.com/quillcraftsman/replay-wizard/blob/main/image.png)

## Backdrop Build

This project was started with [#Backdrop Build](https://backdropbuild.com/v3/replay-wizard) support

<hr>

#### Workflows / Support / Languages
[![Tests](https://github.com/quillcraftsman/replay-wizard/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/quillcraftsman/replay-wizard/actions/workflows/run-tests.yml)
[![Pylint](https://github.com/quillcraftsman/replay-wizard/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/quillcraftsman/replay-wizard/actions/workflows/lint.yml)
/
[![Documentation](https://img.shields.io/badge/docs-0094FF.svg)][documentation_path]
[![Discussions](https://img.shields.io/badge/discussions-ff0068.svg)](https://github.com/quillcraftsman/replay-wizard/discussions/)
[![Issues](https://img.shields.io/badge/issues-11AE13.svg)](https://github.com/quillcraftsman/replay-wizard/issues/)
/
[![Languages](https://img.shields.io/github/languages/count/quillcraftsman/replay-wizard)](https://github.com/quillcraftsman/replay-wizard)
[![Top Language](https://img.shields.io/github/languages/top/quillcraftsman/replay-wizard)](https://github.com/quillcraftsman/replay-wizard)

#### Package / Downloads
[![Version](https://img.shields.io/pypi/v/replay-wizard.svg)](https://pypi.python.org/pypi/replay-wizard/)
[![Development Status](https://img.shields.io/pypi/status/replay-wizard.svg)](https://pypi.python.org/pypi/replay-wizard)
[![Python version](https://img.shields.io/pypi/pyversions/replay-wizard.svg)](https://pypi.python.org/pypi/replay-wizard/)
[![License](https://img.shields.io/pypi/l/replay-wizard)](https://github.com/quillcraftsman/replay-wizardblob/main/LICENSE)
[![Wheel](https://img.shields.io/pypi/wheel/replay-wizard.svg)](https://pypi.python.org/pypi/replay-wizard/)
/
[![Day Downloads](https://img.shields.io/pypi/dd/replay-wizard)](https://pepy.tech/project/replay-wizard)
[![Week Downloads](https://img.shields.io/pypi/dw/replay-wizard)](https://pepy.tech/project/replay-wizard)
[![Month Downloads](https://img.shields.io/pypi/dm/replay-wizard)](https://pepy.tech/project/replay-wizard)
[![All Downloads](https://img.shields.io/pepy/dt/replay-wizard)](https://pepy.tech/project/replay-wizard)

#### Development
[![Release date](https://img.shields.io/github/release-date/quillcraftsman/replay-wizard
)](https://github.com/quillcraftsman/replay-wizard/releases)
[![Last Commit](https://img.shields.io/github/last-commit/quillcraftsman/replay-wizard/main
)](https://github.com/quillcraftsman/replay-wizard)
[![Issues](https://img.shields.io/github/issues/quillcraftsman/replay-wizard
)](https://github.com/quillcraftsman/replay-wizard/issues/)
[![Closed Issues](https://img.shields.io/github/issues-closed/quillcraftsman/replay-wizard
)](https://github.com/quillcraftsman/replay-wizard/issues/)
[![Pull Requests](https://img.shields.io/github/issues-pr/quillcraftsman/replay-wizard
)](https://github.com/quillcraftsman/replay-wizard/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/quillcraftsman/replay-wizard
)](https://github.com/quillcraftsman/replay-wizard/pulls)
[![Discussions](https://img.shields.io/github/discussions/quillcraftsman/replay-wizard
)](https://github.com/quillcraftsman/replay-wizard/discussions/)

[//]: # (#### Repository Stats)

[//]: # ([![Stars]&#40;https://img.shields.io/github/stars/quillcraftsman/replay-wizard)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/replay-wizard&#41;)

[//]: # ([![Contributors]&#40;https://img.shields.io/github/contributors/quillcraftsman/replay-wizard)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/replay-wizardgraphs/contributors&#41;)

[//]: # ([![Forks]&#40;https://img.shields.io/github/forks/quillcraftsman/replay-wizard)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/replay-wizard&#41;)

<hr>

## Menu

- [Install](#install)
- [Quickstart](#quickstart)
- [Mission](#mission)
- [Open Source Project](#open-source-project)
- [Features](#features)
- [Requirements](#requirements)
- [Development Status](#development-status)
- [Contributing](#contributing)

## Install

### with pip

```commandline
pip install replay-wizard
```

See more in [Full Documentation](https://replaywizard.craftsman.lol/install.html)

## Quickstart

### Capture Sequence

```commandline
wizard-capture openyoutube
```

### Replay Sequence

```commandline
wizard-replay openyoutube -d 10 -t true
```

### Combine Sequences

```commandline
wizard-combine three one two
```

### More examples in [Full Documentation][documentation_path]

## Mission

Unlock Efficiency, Replay Your Moves.

Whether you're performing repetitive tasks, testing software, or demonstrating procedures, 
ReplayWizard empowers you to record your actions effortlessly and replay them with precision.

With ReplayWizard, you can automate complex sequences of mouse clicks, keyboard inputs, window movements, and application launches, 
saving you time and effort. Simply initiate the recording, perform your actions as usual, and let ReplayWizard handle the rest.

ReplayWizard offers flexibility and customization, allowing you to edit and refine your recorded actions, adjust playback speed,
and schedule automated tasks for optimal efficiency. Its intuitive interface makes it accessible to users of all levels, 
from beginners to experienced professionals.

## Open Source Project

This is the open source project with [MIT license](LICENSE). 
Be free to use, fork, clone and contribute.

## Features

This features will be built during 4 weeks.
20.03.2024 - deadline

- Capture mouse actions (Done)
- Save mouse actions (Done)
- Replay mouse actions (Done)
- Capture keyboards actions (Done)
- Save keyboards actions (Done)
- Replay keyboards actions (Done)
- Capture environment 
- Save environment 
- Replay environment
- Console script (Done)
- python library API (Done)
- Combine sequences (Done)

## Requirements

- python (library was tested with **3.10**, **3.11** versions)
- pynput (this package use [LGPL-3.0 license](https://github.com/moses-palmer/pynput/blob/master/COPYING.LGPL) and used in this project as a third party library without modifications)
- pydantic

See more in [Full Documentation](https://replaywizard.craftsman.lol/about.html#requirements)

## Development Status

- Package available on [PyPi](https://pypi.org/project/replay-wizard/)

See more in [Full Documentation](https://replaywizard.craftsman.lol/about.html#development-status)

## Contributing

You are welcome! To easy start please check:
- [Full Documentation][documentation_path]
- [Contributing](CONTRIBUTING.md)
- [Developer Documentation](https://replaywizard.craftsman.lol/dev_documentation.html)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Governance](GOVERNANCE.md)
- [Support](SUPPORT.md)

[documentation_path]: https://replaywizard.craftsman.lol