# Disinformation Detection | R Script 02: tidymodels Classifier
# Author: Sawood Anwar
library(tidymodels); library(textrecipes); library(vip)
# rec <- recipe(label ~ text, data = train) %>%
#   step_tokenize(text) %>% step_stopwords(text) %>%
#   step_tfidf(text, num_terms = 500)
# rf_spec <- rand_forest(trees = 500) %>% set_engine('ranger') %>% set_mode('classification')
# wf <- workflow() %>% add_recipe(rec) %>% add_model(rf_spec)
# fit <- wf %>% fit(train)
cat('tidymodels classifier script ready.\n')
