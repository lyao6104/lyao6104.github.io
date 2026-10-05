source "https://rubygems.org"

gem "jekyll", "~> 3"
gem "jekyll-theme-cayman"
gem "kramdown-parser-gfm"
gem "terminal-table"

group :jekyll_plugins do
  gem "jekyll-avatar"
  gem "jekyll-coffeescript"
  gem "jekyll-commonmark"
  gem "jekyll-default-layout"
  gem "jekyll-feed"
  gem "jekyll-gist"
  gem "jekyll-github-metadata"
  gem "jekyll-include-cache"
  gem "jekyll-mentions"
  gem "jekyll-optional-front-matter"
  gem "jekyll-paginate"
  gem "jekyll-readme-index"
  gem "jekyll-redirect-from"
  gem "jekyll-relative-links"
  gem "jekyll-sass-converter"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-titles-from-headings"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
