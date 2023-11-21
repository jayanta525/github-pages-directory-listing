# Github Pages Directory Listing
[![main](https://github.com/jayanta525/github-pages-directory-listing/actions/workflows/main.yml/badge.svg)](https://github.com/jayanta525/github-pages-directory-listing/actions/workflows/main.yml)
[![license](https://img.shields.io/github/license/jayanta525/github-pages-directory-listing)](https://github.com/jayanta525/github-pages-directory-listing/blob/main/LICENSE)
[![Paypal Donate](https://img.shields.io/badge/donate-paypal-00457c.svg?logo=paypal&style=plastic)](https://www.paypal.me/jayanta525)


Generate Directory Listings for Github Pages using Github Actions. 

[Demo](https://github.com/jayanta525/github-pages-directory-listing#demo)

[Read about pages deployment action](https://github.com/jayanta525/github-pages-directory-listing/edit/main/README.md#note)

[action.yml/workflow.yml](https://github.com/jayanta525/github-pages-directory-listing/blob/main/.github/workflows/main.yml)
## Usage
### Getting Started

Add a `.github/workflows/workflow.yml` to the root of your repository.
```
name: directory-listing
on: [push]

jobs:
  pages-directory-listing:
    runs-on: ubuntu-latest
    name: Directory Listings Index
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
        with:
          ref: dummy-data    #checkout different branch

      - name: Generate Directory Listings
        uses: jayanta525/github-pages-directory-listing@v4.0.0
        with:
          FOLDER: data      #directory to generate index

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          path: 'data'      # upload generated folder
  
  deploy:
    needs: pages-directory-listing
    permissions:
      pages: write      # to deploy to Pages
      id-token: write   # to verify the deployment originates from an appropriate source

    # Deploy to the github-pages environment
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    # Specify runner + deployment step
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1
```

### Options
#### Checkout different branch
```
      - name: Checkout Repository
        uses: actions/checkout@v3
        with:
          ref: dummy-data    #checkout different branch
```
#### Checkout different repository
```
      - name: Checkout tools repo
        uses: actions/checkout@v3
        with:
          repository: my-org/my-tools     #repo public url
          path: my-tools                  #folder to clone to
          ref: branch-name               #branch to clone
```
#### Choosing a folder to generate indexing
```
      - name: Generate Directory Listings
        uses: jayanta525/github-pages-directory-listing@v4.0.0
        with:
          FOLDER: data    #directory to generate index
```
#### Refer here for more options: https://github.com/marketplace/actions/checkout

## Note

This action uses Github's own pages deploy action. No gh-pages branch is required.
Under `Settings > Pages > Build & Deployment` 

![image](https://user-images.githubusercontent.com/30702133/226170702-74f11cba-aad2-44ca-9dc5-9f73efd76b41.png)



## Demo
demo URL: https://jayanta525.github.io/github-pages-directory-listing/


### Desktop view

![image](https://user-images.githubusercontent.com/30702133/226169193-66c27c81-fdc7-499d-88e4-1a1c8571ecce.png)

### Mobile View

![image](https://user-images.githubusercontent.com/30702133/226169252-b74d3a40-7928-4804-bd66-8292a6259531.png)


