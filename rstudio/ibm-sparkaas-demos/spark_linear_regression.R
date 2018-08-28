#
# OCO Source Materials
#
# (c) Copyright IBM Corp. 2016
#
# The source code for this program is not published or otherwise divested of
# its trade secrets, irrespective of what has been deposited with the U.S.
# Copyright Office.
#
# File : spark_mtcars.R
############################################################################

library(dplyr)

#data set
View(mtcars)

# copy mtcars data set into Spark
mtcars_tbl <- copy_to(sc, mtcars, overwrite = TRUE, "cars")
colnames(mtcars_tbl)

# list all of the available tables
src_tbls(sc)

# build SQL and execute
library(DBI)
highgearcars <- dbGetQuery(sc, "SELECT * FROM cars WHERE gear >= 5")
highgearcars

# transform our data set, and then partition the data set into 'training', 'test'
partitions <- mtcars_tbl %>%
  filter(hp >= 100) %>%
  mutate(cyl8 = cyl == 8) %>%
  sdf_partition(training = 0.5, test = 0.5, seed = 1099)

partitions$training
partitions$test

# fit a linear model to the training data set
fit <- partitions$training %>%
  ml_linear_regression(response = "mpg", features = c("wt", "cyl"))
fit

summary(fit)
