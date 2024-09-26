# Training and experiments

Tutorials, Python + JavaScript walkthroughs, and examples of various topics. I put this together to make it easier to remember specific things I have done over the years and put them up. However examples are availible for anyone

# Python:

## General topics
* [Functions vs Object Oriented Programming](notebooks/Functions_vs_Object_Oriented_Programming.ipynb)
* [How class (object) inheritance works in Python](notebooks/classes_and_inheritance.ipynb)
* [Multi-processing in Python (not to be confused with async io)](notebooks/parallel_programming_tutorial.ipynb)
* [Creating a simple REST API with Flask](src/flask-app/README.md)
* [Benchmark test of file formats to use when doing Data Analysis](notebooks/File_type_benchmark.ipynb)

## Network Analysis
* [Creating visuals of graphs (using `igraph.plot()`)](notebooks/Visualizing_networks_in_igraph.ipynb)

## Good external resources:
* [Cheatsheet on pandas DataFrame processing (external)](https://www.dataquest.io/blog/large_files/pandas-cheat-sheet.pdf)

-----------


# Repo info

This repository has the following structure

```
├── notebooks               # Notebooks that explore specific concepts
├── src                     # Place for support scripts and python code used for the library
├── data                    # Placeholder folders for the scraped data part of the demo, structure set up but it will be kept local
│   ├── bronze              # For raw data that is collected for any experiments
│   ├── silver              # Semi-processed data converted from the bronze (raw) version
│   └── gold                # Cleaned data that is made available for analysis
└── imgs                    # Folder for images that are rendered in the notebooks
    ├── applying_rap        # Documentation about applying RAP principles to the basic web scraping demo in the notebooks
    ├── images              # Images and diagrams for the documentation
    └── teaching_material   # The actual materials for the 2 sessions
        ├── sept_11         # Slides and latex material for the September 11th virtual session
        └── sept_18         # Slides and latex material for the September 18th in person session
```
