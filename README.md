# python-thursday
This is the package for compiling all of the links into the thursday show notes

#### Requirements:
* python (2.7/3.4)
* BeautifulSoup
* Requests
* chat as '.txt'

#### Document needs:
ensure all links are added in the following syntax:
`> link #category(*optional*\*)

\*if no category is given the link will belong to the previous category. There **MUST** an initial category.

All other text will be ignored. You can also switch back and forth between categories.

> This is some regular text to be ignored
> '> linktosite1 #general' (link will be recognized)
> More random text to be ignored
> linktosite #main (will be ignored, no '>')
> '> linktosite2 #main'
> '> linktosite3 #general'

will produce:

> ##General
>* [sitetitle1]\(linktosite1\)
>* [sitetitle3]\(linktosite3\)
> ##Main
>* [sitetitle2]\(linktosite2\)
