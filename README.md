# Training and experiments

Tutorials, Python + JavaScript walkthroughs, and examples of various topics. I put this together to make it easier to remember specific things I have done over the years and put them up. However examples are availible for anyone

# Python:

## General topics
* [Functions vs Object Oriented Programming](notebooks/Functions_vs_Object_Oriented_Programming.ipynb)
* [How class (object) inheritance works in Python](notebooks/classes_and_inheritance.ipynb)
* [Multi-processing in Python (not to be confused with async io)](notebooks/parallel_programming_tutorial.ipynb)
* [Creating a simple REST API with Flask](src/flask-app/README.md)

## Network Analysis
* [Creating visuals of graphs (using `igraph.plot()`)](notebooks/Visualizing_networks_in_igraph.ipynb)

## Good external resources:
* [Cheatsheet on pandas DataFrame processing (external)](https://www.dataquest.io/blog/large_files/pandas-cheat-sheet.pdf)

-----------


# Repo info

This repository has the following structure

```
├── imgs                    # Folder for images that are rendered in the notebooks
├── data                    # Placeholder folders for any data used in the experiments
│   ├── bronze              # For raw data that is collected for any experiments
│   ├── silver              # Semi-processed data converted from the bronze (raw) version
│   └── gold                # Cleaned data that is made available for analysis
├── src                     # Place for support scripts and python code used for the library
└── notebooks               # Notebooks that explore specific concepts
```
