# Github Pages Directory Listing
[![license](https://img.shields.io/github/license/jayanta525/github-pages-directory-listing)](https://github.com/jayanta525/github-pages-directory-listing/blob/main/LICENSE)
[![Paypal Donate](https://img.shields.io/badge/donate-paypal-00457c.svg?logo=paypal&style=plastic)](https://www.paypal.me/jayanta525)

Generate Directory Listings for Github Pages using Github Actions. 

[Demo](https://github.com/jayanta525/github-pages-directory-listing#demo)
## Usage
### Getting Started

Add a `.github/workflows/workflow.yml` to the root of your project where you want directory listings to be enabled.
```
name: directory-listing
on: [push]

jobs:
  pages-directory-listing-release:
    runs-on: ubuntu-latest
    name: Directory Listings Index
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
        with:
          ref: dummy-data    #checkout different branch

      - name: Generate Directory Listings
        uses: jayanta525/github-pages-directory-listing@v2.0.0
        with:
          FOLDER: data    #directory to generate index

      - name: Deploy to Pages
        uses: JamesIves/github-pages-deploy-action@4.1.3
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          BRANCH: gh-pages
          FOLDER: data
```

### Options
#### Checkout different branch
```
      - name: Checkout Repository
        uses: actions/checkout@v3
        with:
          ref: dummy-data    #checkout different branch
```
#### Choosing a folder to generate indexing
```
      - name: Generate Directory Listings
        uses: jayanta525/github-pages-directory-listing@v2.0.0
        with:
          FOLDER: data    #directory to generate index
```

## Demo
demo URL: https://jayanta525.github.io/openwrt-r4s-kmods/

![image](https://user-images.githubusercontent.com/30702133/184577947-7ebc8b2e-3998-47c7-9289-4069f281f13a.png)
