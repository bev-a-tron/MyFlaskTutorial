Notes
=====

Since any application is nothing other than a way to represent data one should note that there is there is subtle difference between a web application and a desktop application, a desktop application normally is designed to be used by a single person, a web application could be used by millions of people at that same time.

A Desktop application has either a GUI interface or the commandline interface. Web applications provide access ideally on port 80, in that way you don't need a 'client' to access the service that is running on port 80. With flask however you have the freedom to choose the port number, I never had done web programming using a framework before Flask, so it was difficult to understand the basic ideas, in PHP we save the .php files in the 'www' folder, but modern frameworks do not need to place all the projects in one root folder (the www one), the main difference between modern frameworks is there is a modular approach in designing the application, normally in PHP you write code in .php files and link them to each other from various files.

But there is a problem in PHP, giving sexy links (the ones like Quora.com), it is quite difficult to give cute links that are easy to remember, with Flask you get a wonderful way to program web applications.

You create 'links' and then associate with the links a function, you can associate python functions with each 'link' and that function is executed when the link is requested [with GET or POST, for now the difference shouldn't matter at all], there are static assets like HTML pages, CSS or JS scripts. The HTML pages have python markup inside them.
