---
title: ssg-dst
date: 2021-04-12
tags: ssg, code
thumbnail: img/three.jpg
summary: Content that is typically powered by a database, such as comments, sessions and user data can only be handled through third party services.
slug: ssg-data
---

The major downside is that code cannot be executed after a site is created. You are stuck with the output files so if you're used to building web applications with a traditional web framework you'll have to change your expectations.

Content that is typically powered by a database, such as comments, sessions and user data can only be handled through third party services. For example, if you want to have comments on a static website you'd need to embed Disqus's form and be completely reliant upon their service.

Many web applications simply cannot be built with only a static site generator. However, a static website generator can create part of a site that will be served up by a web server while other pages are handled by the WSGI server. If done right, those web applications have the potential to scale better than if every page is rendered by the WSGI server. The complexity may or may not be worth it for your specific application.