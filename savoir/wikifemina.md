---
layout: articles
order: 95
title: WikiFemina
subtitle: En apprendre plus sur le cycle et notre corps tout simplement.
category: Le savoir c'est le pouvoir
alt_img: femme lecture cycle
title_img: "WikiFemina"
og_image: wikifemina.png
previous: /savoir/savoir.html
publish_date: 2021-06-29
---

<div class="index-list">
  {% assign wiki = site.pages | where: "category", "WikiFemina" %}
  {% for p in wiki %}
    <a href="{{ p.url }}" class="list">
      <div class="background bg-rouge">
        <h5 class="title">{{ p.title }}</h5>
      </div>
    </a>
  {% endfor %}
</div>