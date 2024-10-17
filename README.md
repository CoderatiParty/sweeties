#Lemon Drops, Milestone Project 4

(Developer: Richard Messenger)

![Main image](docs/main_img.jpeg)

[Live webpage](https://lemondrops-7ba75e0d4a2a.herokuapp.com/)

Lemon Drops is a satirical news website aiming to capitalise on the prevalence of fake news and dis-information on social media. The site intends to generate revenue by offering a paid subscription service in addition to the free content available to all users.

The website is designed to be accessible and uniform across all devices, allowing clear communication of its exclusive content and subscription options.

## Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
    3. [Developer Goals](#developer-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
3. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colours](#colours)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#testing)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [Accessibility](#accessibility)
    4. [Performance](#performance)
    5. [Device testing](#performing-tests-on-various-devices)
    6. [Browser compatibility](#browser-compatibility)
    7. [Testing user stories](#testing-user-stories)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Project Goals

The key goal is to entertain users, build site traffic and monetise this through paid ads and an ad-free subscription service that offers additional content.

### User Goals

- To enjoy a satirical take on the news
- To cheer themselves up
- To have a giggle
- To be inspired to submit content
- To not have to repeatedly enter my information

### Site Owner Goals

- To entertain
- To provide seamless UX
- To avoid having users submit content
- To package capitalist intent as a friendly news resource in order to separate its users from their hard-earned cash
- World domination

### Developer Goals

- Not to be fired by the evil, hard-nosed capitalists
- Provide a bug free UX
- Easy navigation
- Clear colour contrast for visually impaired users
- Demonstrate competence in web app development
  
[Back to Contents](#Contents)  
  
## User Experience

### Target Audience

- Anyone with a desire to laugh
- Conspiracy theorists

### User Requirements and Expectations

- Reliable, consistent navigation
- No dead links
- Clear presentation across all devices
- Accessibility
- A clear understanding of satire

### User Stories

#### First Visit

- What is going on in the world
- What is this hilarious website all about
- How do I get more of this
- I'm outraged at the facetious content but can't find out how to complain

#### Repeat visit

- Boy, do I need a giggle
- Laughter has cured all my ills and I'd like to cancel my subscription
- I should have signed up the first time
- I'm holding a grudge and maintain a desire to complain whilst festering on my outrage
- Is the data I provide kept private

#### Site Owner

- We want repeat visits
- We want more repeat visits
- We must be more funny
- Give us your money 
- Offer tips on not suing the site owner 
  
[Back to Contents](#Contents)  
  
## Design

### Design Choices

Two distinct layouts have been chosen, with a consistent colour (sic) scheme maintained across the site.

The first layout, found on the home page, extends across the news and account management pages. These are the pages the user will interact with when participating in Lemon Drops' services. On the main homepage, the focus is the satirical news articles. Here, the form is clear, simple and straightforward, to encourage the user to find out more if they choose. 

The second layout is reserved for the 'Corporate Pages' section. These are the obligatory pages all commercial websites must contain. Here, the background colour is pale yellow, a choice consistent with the footer section in the first layout design, where the links to the corporate pages can be found. The intention is to distinguish and guide the user through the use of colour (sic).

A menu, accessible from every page, lists all available pages and alters these options based on whether a user is logged in or not. The intention here, is to simplify the user experience.

Flash messages, using the ubiquitous colour scheme of green for good and red for bad, are used to guide the UX. They are slightly washed out to prevent clashing with yellow.

### Colours

When choosing colours, the focus is on accessibility. A number of combinations were tested using a [contrast checker](https://www.siegemedia.com/contrast-ratio) to make sure a score above 4.5 was achieved for text contrasts. Ideally, we aimed for 7.

A yellow, two-colour scheme is used to compliment the site's name and branding. These are:

Lemon Yellow, #fff700
Pale Yellow, #fefdcf

All text on the site is black, #000000

Main page backgrounds are white, #ffffff

Green flash message background, #00c853

Red flash message background, #e53935

#### Text Ratios

Text on background, main pages (black on white): 21

Text on background, corporate pages (black on pale yellow): 20.16

Text on background, main menu (black on lemon yellow): 18.55

Text on background, header section (black on pale yellow): 20.16

Text on background, green flash message (black on green): 9.38

Text on background, red flash message (black on red): 4.96

### Fonts

To portray Lemon Drops as a media outlet, and present it as an authority, a serif font similar to Times New Roman has been chosen. Selected from Google Fonts, Playfair Display is the only font used on the site.

![Lemon Drops Logo](docs/main_img.jpeg)

### Structure

Every page follows the same basic structure, where the header, footer and 'main' section are consistent, as is the colour scheme, creating an easily identifiable layout for navigational purposes.

As mentioned above, the corporate pages have a pale-yellow background, giving the impression the footer from the main pages has been extended.

On small screens, the sections stack vertically.

The website consists of fifteen distinct pages, organised into the following apps:

##### Home App
 
- index.html: This main page contains the core content the website is built around. Presented as a grid, the list of articles generates automatically every time a new article is added in the admin. The list can be filtered by the categories displayed in the header section.

- article.html: This page is rendered automatically every time a new article is created. It loads when the link in the corresponding headline on the index page is clicked. 

#### Corporate App

- corporate_page.html: The home page for the corporate pages section.
- faqs.html: A page containing answers to common questions the user might ask.
- about.html: A page containing information on Lemon Drops' ethos.
- contact.html: A page containing Lemon Drops' contact information.
- privacy.html: A page containing the privacy statement/policy.
- terms.html: A page containing the terms and conditions.

#### Subscriptions App

- subscriptions.html: This page contains the different subscriptions available to the user, with each being presented in the form of a ticket. The list generates automatically every time a new subscription is added in the admin. As each user is only allowed to own one subscription at a time, if a subscription exists in the user's cart, an alert provides a link to the cart and tells them they will need to remove the subscription from the cart before they can select another. This page does not display if the user has a paid subscription.
- add_subscription.html: A page to confirm the subscription selected on the subscriptions page. It gives the user the opportunity to go back if they wish to change their selection. This page is not accessible if the user has a paid subscription.

#### Profiles App

- profile.html: The user's profile page. Here, they can update their personal details, delete their account and view their previous subscription purchases via a link embedded in the order number, which takes them to the checkout success page, where an alert provides further information.
- delete_confirmation.html: A safety page containing the final delete profile button. The page advises the user of the implications of deleting their account.

#### Cart App

- view_cart.html: This is where added subscriptions are placed ready for the user to purchase. Information contained here is stored in the browser session. On this page, the user has the option to choose whether their subscription is renewed automatically. They are also prompted to login or create an account if they have not done so. Signals are used to retain the integrity of the information in the cart should a user logout before purchasing and to prevent more than one subscription being stored for purchase at any one time.

#### Checkout App

- checkout.html: Here, the user can purchase a subscription once logged in. Their personal information is automatically populated from their profile and they can enter their payment details. An alert provides further confirmation of the purchase amount and provides another opportunity to change their selection.
- checkout success.html: A confirmation page containing the immutable order information. It provides a link to the news section of the website.


### Wireframes

![All Pages](docs/lemondrops_wireframes.png)

![Home Page](docs/home_page_wireframe.png)

![Article Page](docs/article_page_wireframe.png)

![Edit Article Page](docs/edit_article_page_wireframe.png)

![Subscription Page](docs/subscription_page_wireframe.png)

![Add Subscription Page](docs/add_subscription_page_wireframe.png)

![Cart Page](docs/cart_page_wireframe.png)

![Checkout Page](docs/checkout_page_wireframe.png)

![Checkout Success Page](docs/checkout_success_page_wireframe.png)

![Sign Up Page](docs/signup_page_wireframe.png)

![Verify Email Page](docs/verify_email_page_wireframe.png)

![Login Page](docs/login_page_wireframe.png)

![Logout Page](docs/logout_page_wireframe.png)

![Manage Profile Page](docs/manage_profile_page_wireframe.png)

![Delete Confirmation Page](docs/manage_profile_page_wireframe.png)

![Corporate Pages](docs/corporate_pages_wireframe.png)

![Menus](docs/menus_wireframe.png)

![Wide Screen Menu](docs/wide_screemn_menu_wireframe.png)

![Narrow Screen Menu](docs/narrow_screen_menu_wireframe.png)  

![Narrow Screen](docs/narrow_screen_wireframe.png)  
  
[Back to Contents](#Contents)  
  
## Technologies Used

### Languages

- [HTML](https://www.w3.org/html/) - 52.4%
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) - 6.5%
- [JavaScript](https://www.javascript.com/) 2.1%
- [Python](https://www.python.org/) 39%

### Frameworks and Tools

- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Balsamiq](https://balsamiq.com/wireframes/)
- [Adobe Suite (Illustrator, Photoshop & InDesign)](https://www.adobe.com/uk/)
- [Font Awesome](https://fontawesome.com/search)
- [Google Fonts](https://fonts.google.com)
- [Favicon](https://iconifier.net)  
- [W3C validator](https://validator.w3.org/)
- [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/)
- [Text Editor](https://support.apple.com/en-gb/guide/textedit/welcome/mac)
- [Google Chrome](https://www.google.com/chrome/)
- [Apple Voice Over](https://support.apple.com/en-gb/guide/iphone/iph3e2e415f/ios)
- [ChatGPT](https://chat.openai.com)
- [JSLint](https://www.jslint.com)
- [Heroku](https://www.heroku.com)
- [Favicon](https://iconifier.net)  
- [W3 Schools](https://www.w3schools.com)
- [Markdown Editor](https://iwaki.info/markdown-editor-mac/en/index.html)
- [Apple Safari](https://www.apple.com/uk/safari/)
- [Django](https://www.djangoproject.com/)
- [SQL Alchemy](https://www.sqlalchemy.org)
- [VS Code](https://code.visualstudio.com)
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)
- [Amazon AWS](https://aws.amazon.com/)
- [TinyPNG](https://tinypng.com)
- [WAVE Accessibility](https://wave.webaim.org)
  
[Back to Contents](#Contents)  
  
## Features

![Lemon Drops' News](docs/news_articles_users.png)
![Lemon Drops' News](docs/news_articles_staff.png)

- News Display
  - The main feature of the home page, the news articles are organised in a neat grid, can be filtered by category and link to a more detailed report.
  - Python is used to organise the display when a new article is added in admin.
  - It is designed with consideration to accessibility, regarding its font sizes and colour scheme.
  - It uses media query to maintain a viewable arrangement across all devices.
  - Add article button for staff
  - User stories covered: 

![Articles](docs/articles.png)  

- Article Display
  - Displayed in a single column in the middle of the page, white space is left in the margins to give a clean presentation and to allow space for third party advertising.
  - Uses python to automatically render the page based on the information stored in the article model.
  - Edit and delete buttons for staff
  - User stories covered: 

![Manage Profile](docs/personal_details_input.png)  
![Manage Profile](docs/view_past_orders.png) 

- Manage Profile
  - The profile page allows the user to update the information stored in the User_Profile model.
  - They can also delete all information stored by deleting their profile.
  - Access to purchase information is also provided
  - User stories covered: 

![Subscriptions](docs/subscriptions_features_1.png)  
![Subscriptions](docs/subscriptions_features_2.png) 

- Alerts
  - Uses python to guide the users behaviour via alerts, preventing them from adding more than one item to the cart.
  - User stories covered: 

![Cart](docs/cart_features.png)  

- Auto Renew
  - Uses python to give the user the option to auto renew the current purchase.
  - Routing on the login link returns the user to the cart page once logged in.
  - User stories covered: 

![Checkout](docs/checkout_features_1.png)  
![Checkout](docs/checkout_features_2.png)

- Checkout
  - Auto populates the user's information from their profile.
  - User stories covered: 

![Footer Section](docs/footer_section.png) 

- Footer Section
  - The footer contains Lemon Drops' logo, subscription promotion and links to corporate pages.
    - Corporate Information
  - Each page listed in the footer is separate from the main page.
  - The footer is the same on every page and is colour coordinated with the top navigation bar for a visual link.
  - Footer logo uses JavaScript to help the user return to the top of the page.
  - Corporate Pages:
    - FAQ
    - About
    - Contact
    - Terms and Conditions
    - Privacy Statement
  - User stories covered: 

### Future Features To Implement

- Better accredited payment features to enable and build on auto renew function
- Add address information for users to promote and distribute a printed Christmas annual to subscribers
- Consider switching from Django to Flask
- Build bespoke administration interface
  
[Back to Contents](#Contents)  
  
## Testing

All functions work as intended. There are no dead or erroneous links.

When viewed on smaller screens, the sub-sections stack vertically instead of horizontally.

The website was navigated using Apple's Voice Over and aria labels were added to provide a coherent narrative to visually impaired users.

On deploying to Heroku, Django admin css was not exported to AWS and had to be uploaded manually. As Heroku's file system is ephemeral, front end options needed to be added for news article management. An extra model field needed to be added to handle phot uploads.

Some alignment issues were noted when viewed on a phone for the first time and adjusted accordingly using Google Chrome's inspect feature.


### HTML Validation

The templates were put through the W3C Markup Validation Service and returned no errors except for two pages , which are detailed below:

home.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2F)

article.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2F25%2F)

add_article.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fadd%2F)

edit_article.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fedit%2F26%2F)

subscriptions.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fsubscriptions%2F)

add_subscription.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fsubscriptions%2Fadd_subscription%2F1%2F)

view_cart.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcart%2F)

checkout.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcheckout%2F)

checkout_success.html [HTML results](https://validator.w3.org/check?uri=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcheckout%2Fcheckout_success%2F14E67D7337BC4452BE6245C55CBB062A&charset=%28detect+automatically%29&doctype=Inline&group=0)

signup.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Faccounts%2Fsignup%2F)  * Errors on this page correspond to lines that don't exist on the template that was modified: (docs/signup_template.png)

login.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Faccounts%2Flogin%2F)

logout.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Faccounts%2Flogout%2F)

manage_profile.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fprofile%2F)

delete_confirmation.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fprofile%2Fdelete_confirmation%2F)

corporate_pages.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2F)

about.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2Fabout%2F)

faqs.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2Ffaqs%2F) * The error on this page highlights a lack of heading in a section that is the same as the other corporate pages and seems to ignore the FAQs h2 heading further up the page: (docs/faqs_template.png)

contact.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2Fcontact%2F)

privacy.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2Fprivacy%2F)

terms.html [HTML results](https://validator.w3.org/nu/?doc=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2Fterms%2F)


### CSS Validation

The W3C Jigsaw CSS Validation Service passed both stylesheets with no errors.

base.css [CSS results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  

checkout.css [CSS results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcheckout%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  

### Accessibility

For pages that do not require a log in, Lemon Drops passes all accessibility tests with no errors or contrast errors:

home.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/)

article.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/26/)

subscriptions.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/subscriptions/)

add_subscription.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/subscriptions/add_subscription/1/)

view_cart.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/cart/)

signup.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/accounts/signup/)

login.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/checkout/)

corporate_pages.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/corporate/)

about.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/corporate/about/)

faqs.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/corporate/faqs/)

contact.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/corporate/contact/)

privacy.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/corporate/privacy/)

terms.html [Accessibility results](https://wave.webaim.org/report#/https://lemondrops-7ba75e0d4a2a.herokuapp.com/corporate/terms/)

The following pages could not be checked for accessibility becasue they require the user to be logged in to view them:

add_article.html

edit_article.html

checkout.html

checkout_success.html

logout.html

manage_profile.html

delete_confirmation.html


### Performance

Running each page through Google Lighthouse, all pages passed above 90% in all categories:

home.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

article.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2F26%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

add_article.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fadd%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

edit_article.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fedit%2F26%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

subscriptions.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fsubscriptions%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

add_subscription.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fsubscriptions%2Fadd_subscription%2F1%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

view_cart.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcart%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

checkout.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcheckout%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

checkout_success.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcheckout%2Fcheckout_success%2FE16644D88966466598EFC5B8248762B1&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

signup.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Faccounts%2Fsignup%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

login.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Faccounts%2Fsignup%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

logout.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Faccounts%2Flogout%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

manage_profile.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fprofile%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

delete_confirmation.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fprofile%2Fdelete_confirmation%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

corporate_pages.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

about.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2Fabout%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

faqs.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2Ffaqs%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

contact.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2Fcontact%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

privacy.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2Fprivacy%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)

terms.html [Performance results](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Flemondrops-7ba75e0d4a2a.herokuapp.com%2Fcorporate%2Fterms%2F&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo&locale=en-GB&utm_source=lh-chrome-ext)


### Device testing

The website was tested on the following devices:
- MacBook Air
- iPad Mini
- iPhone XR
- iPhone 7
- iPhone 15 Pro

The website was tested using Google Chrome Developer Tools for a selection of popular devices across several manufacturers.

### Browser compatibility

The website was tested on the following browsers:
- Apple Safari
- Google Chrome
- Mozilla Firefox

### Testing user stories

#### First Time Users

1. What is going on in the world

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Page | Click World Category | Requested information is provided | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/select_world.png">   
</details>
<br>

2. What is this hilarious website all about

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Any Page | Scroll down to About link | Link is provided | Works as intended |
| Any Page | Open menu | Link is provided | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/scroll_to_footer.png">  
<img src="docs/open_menu.png">
</details>
<br>

3. How do I get more of this

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Any Page | Open menu | Link is provided | Works as intended |
| Main Page | Scroll down to Footer | Links are provided | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/open_menu_subscribe.png">
<img src="docs/scroll_to_footer.png">  
</details>
<br>

4. I'm outraged at the fatecious content but can't find out how to complain

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Any Page | Scroll down to FAQ link | Information is provided | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/scroll_to_faq.jpeg">  
</details>
<br>

#### Repeat Visit

5. Boy do I need a giggle

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Page | Browse content | Giggle is provided | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/view_content.png">    
</details>
<br>

6. Laughter has cured all my ills and I'd like to cancel my subscription

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Manage Profile | Click button | Information is destroyed | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/delete_profile.png">  
</details>
<br>

7. I should have signed up the first time

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Any Page | Open menu | Link is provided | Works as intended |
| Any Page | Scroll down to Footer | Links are provided | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/open_menu_subscribe.png">
<img src="docs/scroll_to_footer.png">  
</details>
<br>

8. I'm holding a grude and maintain a desire to complain whilst festering on my outrage

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Any Page | Scroll down to FAQ link | Information is provided | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/scroll_to_faq.jpeg">  
</details>
<br>

9. Is the data I provide kept private

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Any Page | Scroll down to Privacy link | Information is provided | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/scroll_to_privacy.png">   
</details>
<br>

#### Site Owner

10. We want repeat visits

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Page | Click link | Add information | Works as intended |
| Add article | Fill out form | Share information | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/click_add.png">  
<img src="docs/fill_form.png">  
</details>
<br>

11. We want more repeat visits

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Page | Click link | Add information | Works as intended |
| Add article | Fill out form | Share information | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/click_add.png">  
<img src="docs/fill_form.png">  
</details>
<br>

12. We must be more funny

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Page | Click link | Add information | Works as intended |
| Add article | Fill out form | Share information | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/click_add.png">  
<img src="docs/fill_form.png">  
</details>
<br>

13. Give us your money

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Any Page | Open menu | Link is provided | Works as intended |
| Main Page | Scroll down to Footer | Links are provided | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/open_menu_subscribe.png">
<img src="docs/scroll_to_footer.png">  
</details>
<br>

13. Offer tips on not suing the site owner

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Any Page | Scroll down to FAQ link | Information is provided | Works as intended |

<details><summary>Evidence</summary>
<img src="docs/scroll_to_faq.jpeg">  
</details>
<br>
  
[Back to Contents](#Contents)  
  
## Bugs

On deployment, it was discovered that Heroku has an ephemeral file system, meaning Django admin could not be used to upload a photo for each article, as was originally planned. To solve this, a workaround was devised whereby an extra image_name column was added to the article and subscription models. The corresponding templates were then updated to use image_name as the image source instead of the url, and, after migrating the changes to the database, this allowed the images stored in Amazon AWS to be displayed.

#### Old Code

Subscriptions models.py:
```
class User_Subscriptions(models.Model):
    """
    Defines the subscription info.
    """
    subscription_type = models.CharField(max_length=12, null=False, blank=False)
    description = models.CharField(max_length=254, null=False, blank=False)
    cost = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    duration_years = models.DecimalField(max_digits=1, decimal_places=0, null=False, blank=False)
    duration_days = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_description = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.subscription_type
```
add_subscription.html
```
<img src="{{ subscription.image.url }}" alt="{{ subscription.image_description }}" class="pic">
```

Home models.py:
```
class Article(models.Model):
    """
    Model for news article info
    """
    category = models.ForeignKey('Category', null=True, blank=False,
                                 on_delete=models.SET_NULL)
    sub_category = models.CharField(max_length=254, null=False, blank=False)
    headline = models.CharField(max_length=1024, null=False, blank=False, db_index=True)
    article_text = models.TextField(null=True, blank=True, db_index=True)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True)
    image_description = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.headline
```
index.html:
```
<img src="{{ article.image.url }}" alt="{{ article.image_description }}" class="pic">
```
##### New Code

Subscription models.py:
```
class User_Subscriptions(models.Model):
    """
    Defines the subscription info.
    """
    subscription_type = models.CharField(max_length=12, null=False, blank=False)
    description = models.CharField(max_length=254, null=False, blank=False)
    cost = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    duration_years = models.DecimalField(max_digits=1, decimal_places=0, null=False, blank=False)
    duration_days = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_name = models.CharField(max_length=254, null=False, blank=False)
    image_description = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.subscription_type
```
add_subscription.html
```
<img src="{{ MEDIA_URL }}{{ subscription.image_name }}" alt="{{ subscription.image_description }}" class="pic">
```

Home models.py:
```
class Article(models.Model):
    """
    Model for news article info
    """
    category = models.ForeignKey('Category', null=True, blank=False,
                                 on_delete=models.SET_NULL)
    sub_category = models.CharField(max_length=254, null=False, blank=False)
    headline = models.CharField(max_length=1024, null=False, blank=False, db_index=True)
    article_text = models.TextField(null=True, blank=True, db_index=True)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True)
    image_name = models.CharField(max_length=254, null=False, blank=False)
    image_description = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.headline
```
index.html:
```
<img src="{{ MEDIA_URL }}{{ article.image_name }}" alt="{{ article.image_description }}" class="pic">
```
#### Results

[Add article form](docs/add_article.png) 

The new field can be seen in the form image above. The defunct field was retained in case of a new service provider. 
  
[Back to Contents](#Contents)  
  
## Deployment

The website was completed using a GitHub repository linked to the VS Code desktop app. Files were committed and pushed to GitHub regularly to backup the files.

Once complete, the following steps were taken to deploy the site from the local server to Heroku:

- Create app in Heroku
- Install DJ Database via terminal command
- Update requirements.txt
- import dj_database_url in settings
- Change default DATABASES in settings to dj_database_url
- Show the migrations in terminal
- Migrate in terminal
- Create a superuser
- Revert default DATABASES to django.db
- Add Procfile
- Install gunicorn via terminal
- Update requirements.txt
- Set account email verification to none in settings to prevent 500 errors
- Install boto3 via terminal
- Update requirements.txt
- Install django-storages via terminal
- Update requirements.txt
- Add 'storages' to installed apps in settings
- Create bucket in AWS
- Add AWS settings in settings
- Create custom_storages.py in root directory
- Login to Heroku via terminal
- Commit changes to GIT
- Update config vars
- Set endpoints and listeners
- Set automatic deploys in Heroku
- Commit changes to GIT
- Add files to AWS once you find out the site looks rubbish
- Implement above bug fix

The Github repository can be found here: <https://github.com/CoderatiParty/sweeties>

The live page on Heroku can be found here: <https://lemondrops-7ba75e0d4a2a.herokuapp.com/>

## Credits

A number of sources were used for the content and media on Lemon Drops website. Images were edited in Photoshop for consistency and theme.

### Content

- Crispy forms supported by Bootstrap: <https://getbootstrap.com>
- ChatGPT for offering solutions to error messages: <https://chatgpt.com>

### Media

- Logo font courtesy of : <https://fonts.google.com>
- Cart and lemon icons provided by: <https://www.fontawesome.com>

### Functionality

- Date functions courtesy of jQuery: <https://jquery.com>
- Return to top courtesy of: <https://www.w3schools.com>

## Acknowledgements

**Written by** ***Richard Messenger***  
  
[Back to Contents](#Contents)  
