# [Code Aquatics](https://code-aquatics.herokuapp.com/)
![Responsiveness](readme_files/images/amiresponsive.PNG)

The main purpose of this project is to create an eCommerce website where users can purchase aquarium related items. This website was made with the beginners' aquarists in mind, here they can find a curated selection of products ideal for beginners and some useful information in a blog.
This website is my fourth and last milestone project for the diploma in software development from the [code institute](https://codeinstitute.net). 
A live view of this website can be found here: [Code Aquatics](https://code-aquatics.herokuapp.com/).

---
## Index
* [UX](#ux)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
* [Features](#features)
  - [Existing Features](#existing-features)
  - [Features to be Implemented in the Future](#features-to-be-implemented-in-the-future)
* [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks and Libraries Used](#frameworks-and-libraries-used)
  - [Databases](#databases)
  - [Testing Tools Used](#testing-tools-used)
* [Testing](#testing)
* [Deployment](#deployment)
  - [Requirements for Deployments](#requirements-for-deployments)
  - [Heroku Deployment](#heroku-deployment)
  - [Hosting Static and Media Files with AWS](#hosting-static-and-media-files-with-aws)
  - [How to Clone the project](#how-to-clone-the-project)
* [Credits](#credits)
  - [Content](#content)
  - [Acknowledgements](#acknowledgements)

---
## UX

### User Stories
* As a generic user, I want a website responsive and good looking on all devices, so I can use it on all devices;
* As a generic user, I want a website easy to navigate so I can find content quickly and easily;
* As a generic user, I want an easily register for an account so I can have a personal account;
* As a generic user, I want to have access to a blog, so a can learn more and feel the need to return to this website to see if there is any new article;
* As a generic user, I want to be able to contact Code Aquatics;
* As a generic user, I want to be able to know more about Code Aquatics;

* As a shopper user, I want to be able to view the list of available products so that I can select some to purchase;
* As a shopper user, I want to be able to search for a product so that I can find it;
* As a shopper user, I want to be able to sort the products by name, price and category so that I can easily identify the best for me;
* As a shopper user, I want to be able to view individual product details such as price, description and rating so that I can decide if that's the product I want to buy;
* As a shopper user, I want to view the total of my purchase at any time so that I can avoid spending too much;
* As a shopper user, I want to easily view the items in my bag so that I can check if I have everything I want;
* As a shopper user, I want to adjust the items in my bag before the checkout so that I can easily make changes before checking out;
* As a shopper user, I want the payment to feel secure, safe and easy so that I can have confidence in this website and a peaceful experience;
* As a shopper user, I want to view an order confirmation after checking out so that I can verify I didn't make any mistakes;
* As a shopper user, I want to receive an email confirmation after checking out so that I can keep records of my purchases;

* As a registered user, I want to receive an email confirmation after registering so that I can verify that my account registration was successful;
* As a registered user, I want to easily recover my password so that I can recover access to my account;
* As a registered user, I want to easily log in and log out so that I can access my account;
* As a registered user, I want to have a personalized user profile so that I can view my details and my order history;

* As a store owner, I want to be able to add a new blog post so that I can make the blog session always fresh and interesting;
* As a store owner, I want to be able to edit any blog post so that I can amend or add information to a post;
* As a store owner, I want to be able to delete any blog post if I feel that there is no need to have that post anymore;
* As a store owner, I want to be able to add a new product so that I can add new products to my store;
* As a store owner, I want to be able to edit any product so that I can change the products' characteristics;
* As a store owner, I want to be able to delete any product so that I can remove items that are no longer for sale;

### Wireframes
It was used [Balsamiq](https://balsamiq.com/) to create the following wireframes:
| Desktop                                                                 | Tablet and Mobile                                                       |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [Home](readme_files/wireframes/desktop-home.png)                        | [Home](readme_files/wireframes/mobile-home.png)                         |
| [Register](readme_files/wireframes/desktop-signup.png)                  | [Register](readme_files/wireframes/mobile-signup.png)                   |
| [Log in](readme_files/wireframes/desktop-login.png)                     | [Log in](readme_files/wireframes/mobile-login.png)                      |
| [Shop](readme_files/wireframes/desktop-shop.png)                        | [Shop](readme_files/wireframes/mobile-shop.png)                         |
| [Product](readme_files/wireframes/desktop-product.png)                  | [Product](readme_files/wireframes/mobile-product.png)                   |
| [Add Product](readme_files/wireframes/desktop-add-product.png)          | [Add Product](readme_files/wireframes/mobile-add-product.png)           |
| [Profile](readme_files/wireframes/desktop-profile.png)                  | [Profile](readme_files/wireframes/mobile-profile.png)                   |
| [Bag](readme_files/wireframes/desktop-bag.png)                          | [Bag](readme_files/wireframes/mobile-bag.png)                           |
| [Checkout](readme_files/wireframes/desktop-checkout.png)                | [Checkout](readme_files/wireframes/mobile-checkout.png)                 |
| [Checkout-success](readme_files/wireframes/desktop-checkout-success.png)| [Checkout-success](readme_files/wireframes/mobile-checkout-success.png) |
| [Blog](readme_files/wireframes/desktop-blog.png)                        | [Blog](readme_files/wireframes/mobile-blog.png)                         |
| [Blog-post](readme_files/wireframes/desktop-blog-post.png)              | [Blog-post](readme_files/wireframes/mobile-blog-post.png)               |
| [Blog-add-post](readme_files/wireframes/desktop-blog-add-post.png)      | [Blog-add-post](readme_files/wireframes/mobile-blog-add-post.png)       |


---
## Features

### Existing Features
The users of this website can be divided into 3 categories: **Unregistered user**, **Registered user** and **Admin**.

All pages share the same header. The **header** contains:
* **search bar**, where the user can search for a product by name or description;
* the information of the **total cost** of the bagged items;
* links to:
  * the **home** page;
  * the **shop**;
  * the **blog**;
* a dropdown menu with the following links:
  * **register** and **login** if the user is an unregistered user;
  * **logout** and **my profile** page if the user is a registered user;
  * **logout**, **add product** and **my profile** page if the user is an admin user;

All pages share the same footer. The footer contains links to social media, to allow the user to know Code Aquatics better, and an email contact, to allow the user to contact Code Aquatics.

The **home** page contains a brief description of Code Aquatics and links to direct the user to the **shop** or to the **blog**.

The **blog** mission is to be informative and interesting. It should make it easier for the user to keep a healthy aquarium and should attract the user to visit the website regularly to see if there are new articles. All blog pages have links to the shop to make it easier for a user to go to the shop. The blog has 4 pages:
* an initial blog page with links to all the blog posts. On larger screens there's also a brief description of the post;
* a blog post page, where the blog post is shown;
* an add blog post page, where the admin user can easily add new blog posts;
* an edit blog post, where the admin user can easily edit existing blog posts. On this page, a prefilled form is shown and the admin only has to change what he wants to edit.
On large screens, the initial blog page and the blog post page has a column where a random product is displayed to invite the user to visit the shop page.
The blog post page has 2 links on the bottom, one to the initial blog page and one to the shop.
The admin user has a link to the **add new post** page on the top of the initial blog page, and links to **edit** and **delete** the blog post for every blog post.
The admin user also has links to **edit** and **delete** the blog post on the blog post page.
When the admin chooses to **delete** a blog post a modal shows up to ensure that the admin user doesn't delete the blog post by mistake.

The **shop** is where the user can see the available products, choose products and proceed to checkout. The shop has 3 pages:
* a **Products** page where all the products are displayed. On this page:
  * the user will see an image, the product's name, the price and the rating for each product;
  * the user will find links to show only the products in each category. This will be shown in a column on large screens and as a dropdown menu on smaller screens;
  * the user can sort the products by name, category or price;
* a **Product** page where a product is displayed. On this page:
  * the user will find an image, a description, the price and rating.
  * the user has the option to select the number of items of the same product to be added to the bag. 
  * If the user is a registered user, the user has the option to rate the product;
  * the user can select the quantity of the product, allowing to buy more than one item at the same time.
  * the user has 2 buttons on the bottom of the product page: one to add the product to the bag and one to return to the Products page. When a product is added to the bag a toast message 'success' with information about the product added, the bag content and the option to go to the bag page is shown.
* an **Edit Product** page, where the admin user can easily edit existing products. On this page, a prefilled form is shown and the admin only has to change what he wants to edit.
Admin users have links to **edit** and **delete** the product on the Products page and on the Product page.
When the admin chooses to **delete** a product, a modal shows up to ensure that the admin user doesn't delete a product by mistake.

The **Bag** page has a list of all the products inside the bag. The user can access the bag page by clicking on the header's bag icon.
Inside the bag page, the user will find information regarding what's inside the bag.
For every product the user will find:
* the product's image;
* the product's name;
* the price of an individual item;
* the option to change the quantity;
* the option to remove the product from the bag;
* the subtotal.
The **Bag** page also has the information on the bag total, the Delivery Cost and the Grand Total.
On the bottom of the **Bag** page the user has 2 options:
  * to keep shopping, if he wants to add more products to the bag;
  * click on the **secure checkout** button and go to the **checkout page**.

The **Checkout** page has:
* delivery information, with the details required such as name, email and delivery address;
* order summary, with the product(s) image, name, quantity and subtotal for every product in the bag and also the order total, delivery cost and grand total;
* a field to insert the payment card details;
* an option the go back and adjust the bag;
* a button to complete the order, if everything is correctly filled. Close to the complete order button, there is information regarding the total cost to be charged.
Once the user completes the order, a checkout_success page will open and a toast message  will be shown.

The **Checkout Success** page contains a thank you message, the user's email where the user will receive a confirmation email and order information with:
* order number;
* order date;
* name and price of every item bought;
* name and delivery address;
* order total, delivery costs and grand total.
At the bottom of the page, the user will find the option to return to the shop.

The **register** page has a link to the sign in page, a form where the user can put the email, username and password.
On the bottom of the register page there's a link to the home page and a button to proceed with the registration.
After the registration is completed, the user will receive an email with a link to confirm the email address. This link gives access to a page where the user can confirm the email.
When the email is confirmed a toast success message is shown and the user is directed to the log in page.

The **log in** page has a link to the register page, allowing the unregistered users to create an account. On the **log in** page the user can log in using the email or the username. If the user can't remember the password he can select a new password by following the link "Forgot Password?".
The **log in** page has a link to the home page and a button to sign in. When the user successfully signs in it's directed to the home page and a toast success message is shown.

All registered users have access to a **profile** page, where the user can store and update the delivery information and check the order history. The order history has information regarding the order number, date, the items bought and the order total.

All users can easily log out using the logout link inside the header's dropdown menu. On the **logout** page there is a confirmation of the user's intents and if the user decides to log out, a toast success message is displayed confirming that the user is no longer logged in.

### Features to be Implemented in the Future
- Change the products and blog input field to allow the shop owner to add several paragraphs, tables and lists without using html.
- Change the blog input field to allow the shop owner to add images to the blog posts.
- Give the registered user the option to repeat previous orders.
---
## Technologies Used

### Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - The programming language used to provide content and structure.
- [CSS3](https://en.wikipedia.org/wiki/CSS)
  - The programming language used to format the styling.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - The programming language used to make the web page interactive.
- [Python (including Jinja)](https://www.python.org/)
  - The programming language used to build the backend functionality.

### Frameworks and Libraries Used
- [Gitpod](https://gitpod.io/)
  - IDE (Integrated Development Environment) used to develop this project.
- [GitHub](https://github.com/)
  - The code hosting platform used to host the project.
- [Django](https://www.djangoproject.com/)
  - Django is used as Python framework for the project.
- [Heroku](https://dashboard.heroku.com/)
  - Cloud platform used to deploy the website.
- [Bootstrap](https://getbootstrap.com/)
  - Open-source CSS framework used to create some layout features in the project.
- [AWS Amazon](https://aws.amazon.com/)
    - AWS Amazon is used to store static and media files.
- [Stripe](https://stripe.com/)
    - Stripe is used for the secure payments 
- [EmailJS](https://www.emailjs.com/)
    - EmailJS is used to send emails to users.
- [Balsamiq](https://balsamiq.com/)
  - The software used to create the project's wireframes.
- [Google Fonts ](https://fonts.google.com/)
  - Font families library used to provide the font "Baloo Tammudu 2" and "lobster".
- [jQuery](https://en.wikipedia.org/wiki/JQuery)
  - JavaScript library used to simplify the JavaScript code.

### Databases
- [SQlite3](https://www.sqlite.org/)
  - SQlite3 is used as the development database.
- [PostgreSQL](https://www.postgresql.org/)
  - PostgreSQL is used as the production database.

### Testing Tools Used
- [Responsive Design Checker](https://www.responsivedesignchecker.com/)
  - Responsive Design Checker was used to test the responsiveness of the site.
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
  - Chrome DevTools was used to test the responsiveness of the site.
- [W3C Markup Validator](https://validator.w3.org/)
  - The markup validation service was used to check for errors in the HTML code.
- [Jigsaw](https://jigsaw.w3.org/css-validator)
  - The CSS validation service was used to check for errors in the CSS code.
- [JSHint](https://jshint.com/)
  - The JavaScript validation service was used to check for errors in the JavaScript code.
- [PEP8 online](http://pep8online.com/)
  - The PEP8 validator was used to check the Python code.

  ---
## Testing

The testing process can be found [here](readme_files/TESTING.md).

---
## Deployment

### Requirements for Deployments
- Python
- GitHub Account
- Heroku Account
- An integrated development environment (IDE)
- Stripe Account
- AWS Amazon Account
- Gmail Account

### Heroku Deployment

- Set up local workspace for Heroku:
  1. In the IDE terminal use the command "```pip3 freeze --local > requirements.txt```" to create a file with the requirements. This file is needed by Heroku to know which files to install.
  2. Create a Procfile with the following text: "```web: gunicorn <name app>.wsgi:application```" This file is needed by Herokuto to know which file is needed as an entry point.
  3. Push all these files to your GitHub repository.
  
- Set up Heroku:
  1. Log in to [Heroku](https://www.heroku.com).
  2. Select 'Create New App' in the top right of the dashboard.
  3. Choose a unique app name, and select the closest region, before clicking 'Create App'.
  4. Go to resources in Heroku and search for postgres. Select Hobby dev - Free and click on the provision button to add it to the project.
  5. Go to the settings app in Heroku and go to **Config Vars**. Click on **Reveal Config Vars** and add the following config variables:
  
    | KEY                   | VALUE                                  |
    |-----------------------|----------------------------------------|
    | AWS_ACCESS_KEY_ID     | `<aws access key>`                     |
    | AWS_SECRET_ACCESS_KEY | `<aws secret access key>`              |
    | DATABASE_URL          | `<postgres database url>`              |
    | EMAIL_HOST_PASS       | `<email password(generated by Gmail)>` |
    | EMAIL_HOST_USER       | `<email address>`                      |
    | SECRET_KEY            | `<your secret key>`                    |
    | STRIPE_PUBLIC_KEY     | `<your stripe public key>`             |
    | STRIPE_SECRET_KEY     | `<your stripe secret key>`             |
    | STRIPE_WH_SECRET      | `<your stripe wh key>`                 |
    | USE_AWS               | `True`                                 |


- Set up Database
  1. Copy the **DATABASE_URL** (Postgres URL) from the config variables of Heroku and past it into the default database in `setting.py`

  ```
  DATABASES = {
    'default': dj_database_url.parse("<DATABASE_URL here>")
  }
  ```
  
    **NOTE:** This setup for the databases is temporary for deployment to Heroku.
  2. Migrate the models to create the database by the following commands:
        - `python3 manage.py makemigrations`
        - `python3 manage.py migrate`
  3. Load the data fixtures for categories and products in this exact order:
        - `python3 manage.py loaddata categories`
        - `python3 manage.py loaddata products`
  4. Create a superuser. The superuser has access to the admin environment.
        - `python3 manage.py createsuperuser`
        - Enter your username, email and password.
  5. Now you can remove the DATABASE_URL from `settings.py` and set the previous default DATABASE settings.
  6. Adjust the ALLOWED_HOSTS in your settings.py with the following:
    
    ```
    ALLOWED_HOSTS = ['<your Heroku app URL>', 'localhost]
    ```

  7. Push the code to Github.

- Connect with Heroku:
  1. Click on the **Connect to GitHub** section in the deploy tab in Heroku. 
  2. Search your repository to connect with it.
  3. When your repository appears click on **connect** to connect your repository with the Heroku. 
  4. Set automatic deployment: 
    - Go to the deploy tab in Heroku and scroll down to **Automatic deployments**.
    - In the `Deploy` tab, click `Enable Automatic Deployment`.
    - In `Manual Deploy`, choose the master branch.
    - Click `Deploy Branch` to deploy the app onto the Heroku servers.
    - Heroku will receive the code from Github and host the app using the required packages. 
    - Click on `Open app` in the right corner of your Heroku account. The app will open and the live link is available from the address bar. 

### Hosting Static and Media Files with AWS
The static and media files are hosted in the AWS S3 Bucket. To host them you will need an account and create an S3 bucket and set a group, policy and user in the IAM environment. 
Read more about the S3 Bucket storage [here](https://aws.amazon.com/s3/). For more information about the storage in your project [click here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).


### How to Clone the Project:
To run the code locally by __cloning__ the project from GitHub:
- Log into your [GitHub](https://github.com/) account;
- Find and choose the Repository for this project (RuiOliveira83/MS4_Code_Aquatics);
- Inside the Code button copy the URL link inside the Clone section;
- Open repository or create a new repository;
- Open terminal;
- Type `git clone` followed by the copied URL and press Enter.
- Create an env.py file with the following values:
``` python
import os

    os.environ("SECRET_KEY", "Added by developer")
    os.environ("STRIPE_PUBLIC_KEY", "Added by developer")
    os.environ("STRIPE_SECRET_KEY", "Added by developer")
    os.environ("STRIPE_WH_SECRET", "Added by developer")
    os.environ("AWS_ACCESS_KEY_ID", "Added by developer")
    os.environ("AWS_SECRET_ACCESS_KEY", "Added by developer")
    os.environ("DATABASE_URL", "Added by developer")
    os.environ("Database", "Added by developer")
```
- Add the `.env` file to the `.gitignore` file.
    **NOTE:** See more in the [Stripe Documentation](https://stripe.com/docs/keys) to read more about setting the API key.
- Migrate the models to create the database by the following commands:
  - `python3 manage.py makemigrations`
  - `python3 manage.py migrate`
- Load the data fixtures for categories and product in this exact order:
  - `python3 manage.py loaddata categories`
  - `python3 manage.py loaddata products`
- Create a superuser. The superuser has access to the admin environment.
  - `python3 manage.py createsuperuser`
  - Enter your username, email and password.
- Run the app: Open your terminal window in your IDE. Type: `python3 manage.py runserver` and run the app.
- To access the admin environment, you can add `/admin` at the end of your url and login with the superuser.

---
## Credits

### Content

- Overall structure:
  - The boutique Ado project was used as a guideline throughout the building of this website.
  - I've looked at several aquarium shops websites such as [Aquaristic Net](https://www.aquaristic.net/) and [Aquaristik Shop](https://www.aquaristikshop.com/) for inspiration and products images and details.
- Read me file:
  - I used the code institute template and followed my previous project as a guideline.

### Acknowledgements
- The [Code Institute](https://codeinstitute.net) for the inspiration and knowledge to do this website.
- The Code Institute [Slack](https://slack.com/) channel, for having an extensive library of questions and answer with almost all my questions.
- The  [Code Institute](https://codeinstitute.net) tutors for all the help.
- My mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for guidance and support.
