CREATE OR REPLACE TABLE `project_id.dataset_id.agg_users`
(
  creation_date TIMESTAMP,
  user_name STRING,
  badge_name STRING,
  reputation INT64,
  up_votes INT64,
  down_votes INT64,
  views INT64
)
PARTITION BY
  TIMESTAMP_TRUNC(creation_date, MONTH);