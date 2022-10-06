# crawldiversden
Crawls Divers Den by LiveAquaria to Anticipate Newly Uploaded Products.

DiversDen by LiveAquaria hosts a What You See Is What You Get (WYSIWYG). The products (often fish or crustacea) are in limited quantity (each product
has an inventory of 1) and can quickly sell out once released. However, in order to meet a shipping minimum for Free Shipping or Discounts, one 
must reach a certain price in one's cart. This decision on what products one should add in the cart can be helped by:

crawldiversden.py which can be used usually at least an hour or two before the anticipated release of the products to see uploaded images
of the products that will soon be added to the inventory of DiversDen, allowing users to decide if its worthwhile to attempt to buy these items
and prepare in advance for them by giving future knowledge.

crawldiversden.py does this by checking various possible image names based on previously used image name formats, which accounts for date,
by LiveAquaria and attempting to see if a image is valid or not. This works because the website uploads future products to public access
before the product is even available to find on their website.
