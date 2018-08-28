#
# OCO Source Materials
#
# (c) Copyright IBM Corp. 2016
#
# The source code for this program is not published or otherwise divested of
# its trade secrets, irrespective of what has been deposited with the U.S.
# Copyright Office.
#
# File : spark_kernel_basic.R
############################################################################

# create local R data frame
library(dplyr)
localDF <- data.frame(name=c("John", "Smith", "Sarah", "Mike", "Bob"), age=c(19, 23, 18, 25, 30))

#create Spark kernel data frame and temporary table based on local R data frame
sampletbl <- copy_to(sc, localDF, "sampleTbl")

# list tables
src_tbls(sc)

#db query for sampleTbl table
library(DBI)
sampletbl_preview <- dbGetQuery(sc, "SELECT * FROM sampleTbl")
sampletbl_preview

# filter by age
filtered_sampletbl <- sampletbl %>% filter(age > 20)
filtered_sampletbl

# reading data
iris_tbl <- copy_to(sc, iris, "irisData")

# list tables
src_tbls(sc)

library(DBI)
iris_preview <- dbGetQuery(sc, "SELECT * FROM irisData")
iris_preview
