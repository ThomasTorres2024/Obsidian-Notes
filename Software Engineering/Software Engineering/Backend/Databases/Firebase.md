Firebase is a NOSQL base, and uses documents of Json to store its information. We have collections, tasks and users. Tasks are like tables where we put things in a spot.  Instead of rows, we have json files of the data. This is very different from SQL databases. Every time the user makes a task we store information about the task 

All the thing wants is the title, and then some extra info if we need it. Data is tied to a user, also stores uid. We also use firebase authentication to confirm email and password login. Gives us a unique ID for who someone was. Document owner is the user who owns a record assosciated with their name 

Users need to be authenticated. We need a very basic profile, their name, their profile picture etc. We need a collection to store this info. Users doesn't store password just their info, name, UID etc. Also we have a creation time. 

We will also store profile pictures using firebase storage. Firebase gets an image in the storage, and then we we get a url to an image in storage. 

Flutterflow has built in firebase integration. We have a config file usually, we have to enable these features and do multiple things on top of that Flutter has the ability for us to manage the DB inside of flutter as well that is an option. 

---

When developing a backend its important to put it in a proper database schema. If we have some kind of schema for how our database should look, it helps AI agents understand what we are doing. We need to be able to design documentation for others to get caught up as well. We will take 

When  we lay out a schema, we have instead of a true value an explanation of the values at each entry. 