Fieldwork Model Evaluation Step
===============================

MAP Client plug-in for evaluating a fieldwork model at a regular
discretisation.

Requires
--------
None

Inputs
------
- **ju#fieldworkmodel** [GIAS2 Fieldwork Geometric Field instance] - a
fieldwork model to be evaluated.

Outputs
-------
- **pointcloud** [nx3 NumPy Array] - An array of point coordinates evaluated
at a regular discretisation on the fieldwork model.

Configuration
-------------
- **identifier** : Unique name for the step.
- **discretisation** [list of ints]: The number of regularly-spaced points to sample in
each element coordinate direction in each element of the fieldwork model.
Should be of the format [d_1, d_2, ..., d_n] where d_i is the number of
points to be sampled in element coordinate direction i. For example, to
sample 10 by 10 points in each element in a 2-D surface mesh: [10,10]. 
- **node coordinates** [True|False] - Whether to return the model node
coordinates instead of discretised points.
- **elements** - In which elements to evaluate the fieldwork model. Can
be either
    - 'all' to evaluate all elements
    - A series of comma-separated integers and ranges defining the elements
    to evaluate, e.g. 1,2,5-10.   

Usage
-----
This step is used to discretise a fieldwork mesh model into a pointcloud
by sampling elements at regular intervals in each element's local coordinate
system.

To discrete a fieldwork model for triangulation, use Fieldwork Model
Triangulation Step.
