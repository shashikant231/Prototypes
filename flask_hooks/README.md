# Hooks in Flask


**App and Blueprint** 

Flask app is the main application object . It handles requests and route it to appropriate views. It manages config and running of server.


Blueprint : consider it as mini-app inside main application. it helps in splitting large codebase into smaller modules by feature(orders, users, payment..)


Blueprint needs to be registerd inside main application.

Now coming back to hooks ...

Think of Flask hooks as automatic function that run at specific stage of request/response lifecycle. we don't have to call this func manually, flask calls them for us. 


How do use these hooks?

Hooks can be global (app level) or local (blueprint level)

Inside our app.py , we have two app level hooks : 

* before_request : runs before every request
* after_request : runs after every request

This hooks will be run for every request inside the main application or any blueprint registerd inside main application.

For eg: In users module , when we call api */users* these hooks will get executed.

But what if we want to add hooks only for blueprint , then we will need blueprint level hooks. This hook will be called before any app level hook .

For eg , for users module , we have added a before_app_request hook that monitor request to this module.
