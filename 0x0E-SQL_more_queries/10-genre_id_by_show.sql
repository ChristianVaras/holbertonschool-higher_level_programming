-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT ts.title, tsg.genre_id
      FROM tv_shows AS ts
      JOIN tv_show_genres AS tsg
      ON ts.id = tsg.show_id
      ORDER BY ts.title, tsg.genre_id;
