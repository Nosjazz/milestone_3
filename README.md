<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome Nosjazz,

[View the live project here.](https://data-3.herokuapp.com/home)

This website has been created in order to complete the 3rd milestone project of the code institute fullstack diploma. This is a prelaunch website with a landing page centralizing the information, a About page giving more information about the project, a reviews page to centralize all reviews written, a contact us page, and a login/logout function.  HTML, CSS, JS, Python and MongoDB as well as Flask and Jquery were used. 


## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the project, leave if review and have the option to contact the website owner directly.
        2. As a First Time Visitor, I want to be see a visually compellent design.
        3. As a First Time Visitor, I want to be able to see reviews from other visitors.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to find back the information I entered

-   ### Design
    -   #### Colour Scheme
        -   The main colours used are blue and white to have a high contrast, low eyes strain application.
    -   #### Typography
        -   The Poppins font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Poppins is a simple font that is appealing for this purpose.
        
    -   #### Imagery
        -   No images were used for this project to keep the simple and neutral effect desired.

*   ### Wireframes

    -   Home Page [Wireframe](https://github.com/Nosjazz/todo_list-milestone2/blob/master/assets/pictures/wireframe.jpg). Due to time contraints, the project was adaptated to conserve the minimum features, removing the weekly and monthly tracking and the second filtre by date.

## Features

-   Responsive on all device sizes

-   Interactive elements

-   Add items

-   Filter items by All, Completed, uncompleted

-   Complete items

-   Trash items

-   Refresh all items

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Font Awesome icons to add the color and rotation transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Poppins' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - No error
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - No error
-   [JShint validator](https://jshint.com/) - No error, 27 warnings

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the application and learn more about the organisation and feature.

        1. Upon entering the website, the user is invited to add an item with the placeholder
        <img src="./assets/pictures/placeholder.JPG">
        2. When hovering into the + button next to the add item, their is a visual clue that indicate to the visitor the function to add an item is by clicking this button
        <img src="./assets/pictures/add_hover.JPG">
        3. Once the first item is added, the 2 buttons next to the item have the same visual to create consistancy to the user
        <img src="./assets/pictures/item_hover_done.JPG">
        <img src="./assets/pictures/item_trash_done.JPG">
        4. When the user complete a task, the opacity is reduce and the text is barred
        <img src="./assets/pictures/item_completed_ok.JPG">

    2. As a First Time Visitor, I want to be see a visually compellent design and animations.

        1. The design is left simple without image in the background and a simple gradient with cold colours to ease strain on the eyes
        <img src="./assets/pictures/gradient.JPG">
        2. The different actionnable item has the color of the end gradient to keep consistency for the user
        3. Each actionable item has an hover effect and transition 
            a. Transition of height and width when deleting item
            b. Transition of delay when completing an item
            c. Rotation of the refresh button on hover
            d. Color transition when hovering other items
            e. Change of pointer when hovering over items

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find back the information I entered

        1. With local storage implemented, items are saved so that user will keep the items previously entered without the need to sign in

    2. As a Returning Visitor, I want to find a way to filter between ongoing and completed activities.

        1. The filter option allows the visitor to show all items, completed , or uncompleted ones
        <img src="./assets/pictures/filter.JPG">

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to be able to refresh all the items added at once.

        1. The refresh item on top right corner allows the user to remove all items at once

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all functions were working correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   On Internet Explorer Browsers, the site is not functional
-   When the item contains several lines, the icons are not aligned middle
-   When clicking on the List element, having unkown error in the console.
-   When deleted a todo element, having an error in the console.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Nosjazz/todo_list-milestone2)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Nosjazz/todo_list-milestone2)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Nosjazz/todo_list-milestone2)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/Nosjazz/todo_list-milestone2
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/Nosjazz/todo_list-milestone2
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   [Tutorial 1](https://www.youtube.com/watch?v=b8sUhU_eq3g) : Main Javascript features were based upon this Tutorial
-   [Tutorial 2](https://www.youtube.com/watch?v=Ttf3CEsEwMQ&t=2510s) : Additional features and CSS were based upon this Tutorial

### Content

-   All content was written by the developer.

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.