# python-thursday
This is the package for compiling all of the links into the thursday show notes

## Requirements:
* python (2.7/3.4)
* BeautifulSoup
* urllib
* chat in file

### Setting Categories
The default category is "Uncategorized". To set a new category. Enter the "#" Followed by the Category. The whole line will be accepted as the category.

### Setting Links:
To add a link just enter the link by itself. There is no need for a title, as pt shownotes will find one for you. 

Accepted Links:
* http://www.link.com
* https://www.link.com
* www.link.com
* link.com

If a link fails to be read (i.e. bad syntax or false detection of a link). A "*\<link\>* Failed" will be returned and it will process the next link.

All links will belong to the previous set category

####Example
> This is some regular text to be ignored
>  \#Category1
> More random text to be ignored
> linktosite1.com
> www.linktosite.com 
> \#Category2
>https://linktosite3/web/blog/otherthings?test

will produce:

> ##Category1
>* [sitetitle1]\(linktosite1.com\)
>* [sitetitle2]\(www.linktosite.com\)

> ##Category2
>* [sitetitle3]\(https://linktosite3/web/blog/otherthings?test\)
