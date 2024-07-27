# Playwright_sync
# Registration Form Automation Tests

This repository contains a set of automated tests using Playwright to validate the functionality of the registration form on the OrangeHRM, automationtesting.
(https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
(https://demo.automationtesting.in/Register.html).


## Introduction

This project demonstrates how to use Playwright to automate browser interactions for testing a registration form. The tests cover various form fields such as first name, last name, address, email, phone number, skills, date of birth, and language selection. Use of automated code generator of playwright.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Node.js](https://nodejs.org/en/) (which includes npm)
- [Python](https://www.python.org/) (for running pytest)
- Basic understanding of JavaScript or TypeScript

## Installation

Follow these steps to set up the project:

1. Clone this repository:

    ```sh
    git clone https://github.com/yourusername/registration-form-automation.git
    cd registration-form-automation
    ```

2. Install the necessary dependencies:

    ```sh
    npm install
    ```

3. Install Playwright:

    ```sh
    npx playwright install
    ```

## Usage

The test scripts are located in the `tests` folder. They use Playwright to perform various actions on the registration form and validate the results.

## Code generator

```sh
playwright codegen
```

## Running the Tests

To run the tests, use the following command:

```sh
npx playwright test
```
