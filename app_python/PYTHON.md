# Best practices used
- Followed Django standard project structure and guidelines
- Used linters & formatters during development
- Followed PEP-8, especially naming conventions (about short understandable names)
- Used venv for this project

# Framework
I chose Django framework because it provides lots of web capabilities out of the box. 
Also, I wanted to have a clear structure imposed by the framework.

Advantages of Django:
- Build-in functionality which includes routing, security
- Scalability which allows to add more hardware with no effect on other components

Disadvantages:
- Django is monolithic which makes it hard to customize against the standard conventions
- Not suitable for small and fast projects since it adds some overhead

# Linters
Mainly I used [Pylint](https://pypi.org/project/pylint/) and [mdl](https://github.com/markdownlint/markdownlint).
Also, I used default Pycharm formatter.

# Unit tests
This app contains 2 tests:
- `test_moscow_time()` is a unit test for verifying that returned time is of Moscow
- `test_home_page_view()` is technically an integration test for testing that django view returns 200

Best practices:
- Creating separate directories for tests. Test file structure mirrors project structure
- Keeping tests simple - they should test as isolated functionality as possible
- Integrating testing into CI