# KickScraper

This project offers an API to consult Kickstarter projects information. It does that by scrapping the website so this software is provided as it is. No guarantee is assured.

To check everything is working correctly and the needed data is able to be pulled from the Kickstarter page, from the project root execute:

`PYTHONPATH=. py.test`

# Class Reference

## Project

- Project.uid: int
- Project.title: str
- Project.photo: dict
- Project.pledged: float
- Project.goal: float
- Project.state: str
- Project.currency: str
- Project.launched: int (unix time)
- Project.deadline: int (unix time)
- Project.backers\_count: int
