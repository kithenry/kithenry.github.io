# List of items to check off for site to be good enough
1. Define what a portfolio site is and from that list the most crucial elements
2. Collect components that you'll need for yours
    1. Create folder structure to store site content #action
    2. Add to it what resources you have 
    3. Hunt online for what you don't 
3. Define some basic site template for site 
4. Wireframe the site using draw.io (desktop and mobile sections)
5. Write in VSCode the index.html page html for the site
6. Design the site (for desktop only for now)
    1. Figure out what bootstrap compoents will be used
    2. Figure out what font will be used
    3. Setup bootstrap
    4. Open links to documentation explaining how to use all bootstrap components you'll use
    5. Build based off template design
7. Replace all lorem ipsum with actual content.
8. Schedule responsiveness (Mobile design, tab design)


## 1.1 What it is
- A website to showcase and highlight one's work, achievements, skills, and experiences. A digital gallery or resume that allows one to visually present their work and skills to potential clients, employers, collaborators, or followers. [sendpulse](https://sendpulse.com/blog/portfolio-websites). It is tailored to the job one wants to apply to and can include more skills than the recruiter needs but should have a filter section for them to select relevant information [mitcommalab](https://mitcommlab.mit.edu/meche/commkit/portfolio/)

### 1.2 What to show
- Profile picture (in portfolio_assets)
- Short bio details section (to be linked to via about in header)
- Projects (Bududa Web Project) (one project per page if multiple)
- Internships (nil)
- Academic Achievements (in about me section)
- Work experience (student assistantship, project management)
- CV (to be linked at the end of about me detail)
- About me in more detail (about page)
- Link to personal work outside profession (about page)

#### 1.2.1 Where to show what (pages and their content)
`Content here will initially be lorem ipsum`
- Landing Page (Page User is greeted by when they visit my website, `index.html`)
    - Will have a header with links to my projects page, gallery and about pages
    - Will have a profile picture of me with a greeting and short bio to its side
    - Will be what `Projects` button leads to
- Gallery Page (Tiles showing links to projects, `gallery.html`)
    - Will have all projects that can't fit on the home page
    - Will be what the `show more projects` button leads to
- About Page (More detailed whoami, `about.html`)
    - Will have a picture of me to the right of a blob of text
    - The blob of text will be an averagely detailed summary of who I am.
        - where i am now and who i am working as if working at all
        - story of interests evolution and current dreams
        - what i do outside work
        - links to my resume and call to send me an email, using a mail:to href

## 2 Collecting components that'll be needed
- All components from 1.2 (profile image, cv, [link to project](https://kithenry.github.io/projects/index.html))

## 3 Template to use
- Adapted from (https://www.alyssali.me/)

## 4 Site Wireframe
- Wireframe file in portfolio_assets folder (Portfolio Website Wireframe.drawio) drawn using draw.io

## 5 Writing HTML For Site
- Create empty html files for all pages
- Write boiler plate for each page
- Add sections and divs based on wireframe for each page
    - add descriptive class names to divs and sections
    - find and make list of bootstrap elements that'll be used for components
        - [bootstrap cards](https://getbootstrap.com/docs/4.0/components/card/) will be used for tiles in the project tiles section.
        - this snippet
        ```html
         <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Bootstrap demo</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">

        ```
         will be added to header of each file to allow rendering of bootstrap code

- Add lorem ipsum content to divs and link images.




