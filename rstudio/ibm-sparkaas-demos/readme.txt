#
# OCO Source Materials
#
# (c) Copyright IBM Corp. 2016, 2017
#
# The source code for this program is not published or otherwise divested of
# its trade secrets, irrespective of what has been deposited with the U.S.
# Copyright Office.
#############################################################################
# File : readme.txt
############################################################################

Three example R script files demonstrate how the Spark service works in RStudio:
 
 1) spark_kernel_basic.R   :- Creates simple R data frames and generates remote Spark data frames based on the local R data frames. It also runs some basic filters and DBI queries.
 
 2) spark_mtcars.R :- Loads the popular mtcars R data frame and then generates a Spark data frame for the  mtcars data frame. It then does transformations to create a training data set and runs a linear model on the training data set.
 
 3) spark_flights.R :- Loads some bigger data sets about flights and batting. This scenario is taken from http://spark.rstudio.com/index.html. The script creates a ggplot plot for delay and runs window functions.
