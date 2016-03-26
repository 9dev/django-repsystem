# django-repsystem

Simple reputation system for Django.

## Installation

- Add `repsystem` folder to Python path.
- Add `"repsystem"` to your `INSTALLED_APPS`.

## Usage

### Defining actions and levels

Firstly, you should define actions that are going to be rewarded with reputation points as well as levels that your users can achieve.

It's recommended to create them via a fixture. For example:

    ```
    # file my_fixture.json
    
    [
        {
            "model": "repsystem.action",
            "pk": 1,
            "fields": {
                "name": "article_published",
                "message": "Publishing a new article",
                "value": 10
            }
        },
        
        {
            "model": "repsystem.level",
            "pk": 1,
            "fields": {
                "name": "Beginner",
                "required_rep": 0
            }
        },
        {
            "model": "repsystem.level",
            "pk": 2,
            "fields": {
                "name": "Master",
                "required_rep": 100
            }
        }
    ]
    ```

### Admin panel access

User's reputation score and level are going to appear in User section in Django admin panel for easy reference.

Of course, raw access to `repsystem` models is also provided.

### Displaying user's reputation or level

If you need to show user's level or score in a template, you could write something similar to:


    {% if user.is_authenticated %}
        Your reputation: {{ user.reputation.score }},
        Your level: {{ user.reputation.level.id }} - {{ user.reputation.level.name }}
    {% endif %}

### Rewarding users with reputation points

When user performed some desired action, you should call `perform_action` function in order to take it into account and log it in user's history:

    
    from repsystem.utils import perform_action

    def my_view(request):
        ...
        perform_action(self.request.user, 'article_published')
        ...
   
### Leveling up

System will automatically discover when user gathered enough reputation and will level him up.

### Changes history

If you want to create a history of user's changing reputation, you can use `get_user_history` function:


    from repsystem.utils import get_user_history

    def my_view(request):
        ...
        context['history'] = get_user_history(self.request.user)
        ...


Example usage in a template:


    {% for item in history %}
        <p>
            {{ item.creation_date }} :
            You got <strong>{{ item.action.value }}</strong>
            reputation points for: {{ item.action.message }}.
        </p>
    {% endfor %}
    
### Notes

- If you update existing actions, reputation history may become incorrect as it uses foreign key to Action model.

- If you are using this app in a project with existing User objects, you should also create a fixture containing one Reputation object for each of your users (see example in demo project).

## Demo

`django-repsystem` provides a simple demo with example usage. To install it from the console, execute `fab install` command. To run it, type ``fab runserver``.

Of course, to do that you need to have `fabric` installed on your computer.

## Tests

Tests assume that Selenium's ChromeDriver can be found at:
> /usr/bin/chromedriver

It also needs correct permissions. Make sure to run:

    $ sudo chmod a+x /usr/bin/chromedriver

To run all the tests simply type:

    $ fab install
    $ fab testall

## Notes

This package was tested with Python 3.4 and Django 1.8.

## License

MIT

