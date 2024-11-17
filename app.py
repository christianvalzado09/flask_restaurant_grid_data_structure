from flask import Flask, render_template

app = Flask(__name__)


# TODO: Restaurant List of Dictionaries
# image_url, restaurant_name, status, location, id
restaurants = [
    {
        "id": 1,
        "location": "Makati",
        "restaurant_name": "Restaurant One",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 2,
        "location": "Pasig",
        "restaurant_name": "Restaurant Two",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/25858122/pexels-photo-25858122/free-photo-of-patio-of-cafe.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 3,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Three",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16550341/pexels-photo-16550341/free-photo-of-facade-of-urban-building.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 4,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Four",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/12935080/pexels-photo-12935080.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 5,
        "location": "Alabang",
        "restaurant_name": "Restaurant Five",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/8921562/pexels-photo-8921562.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 6,
        "location": "Pasig",
        "restaurant_name": "Restaurant Six",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },
  {
        "id": 7,
        "location": "Manila",
        "restaurant_name": "Restaurant Seven",
        "status": "Closed",
        "image_url": "https://i.pinimg.com/originals/e8/60/e9/e860e96419268ea9d4c6f2e768f554b1.jpg"
    },
    {
        "id": 8,
        "location": "Cebu",
        "restaurant_name": "Restaurant Eight",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.0Y_7e4c2Rfs4OGFLLF74MAHaE8?w=296&h=197&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 9,
        "location": "Davao",
        "restaurant_name": "Restaurant Nine",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.4N6JxbMRT_LE25grjVXH5QHaFU?w=341&h=197&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 10,
        "location": "Baguio",
        "restaurant_name": "Restaurant Ten",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.fORormXH8F4RrGfGKna1FwHaEO?w=288&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 11,
        "location": "Makati",
        "restaurant_name": "Restaurant Eleven",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.AIfaApTjXkZYO23toY6BwwHaEK?w=303&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 12,
        "location": "Pasig",
        "restaurant_name": "Restaurant Twelve",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.Reel7wILD5Nn-YCj9JSJ3wHaE4?w=233&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 13,
        "location": "Quezon City",
        "restaurant_name": "Restaurant Thirteen",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.-lyObdkp8zo-p1h7OyOUdAHaE8?w=284&h=189&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 14,
        "location": "Pasay",
        "restaurant_name": "Restaurant Fourteen",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.7fvmnhK104QWUMHHTHP9pAHaE7?w=250&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 15,
        "location": "Muntinlupa",
        "restaurant_name": "Restaurant Fifteen",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.qE32mi6tEwHRLu91KHl4LgHaE8?w=229&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 16,
        "location": "Las Piñas",
        "restaurant_name": "Restaurant Sixteen",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.UzdSvG0BMmluALF_btyskwHaDt?w=306&h=175&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 17,
        "location": "Cavite",
        "restaurant_name": "Restaurant Seventeen",
        "status": "Closed",
        "image_url": "http://ts1.mm.bing.net/th?id=OIP.9couaiy_0iUBOr5V3d8VugHaEK&pid=15.1"
    },
    {
        "id": 18,
        "location": "Parañaque",
        "restaurant_name": "Restaurant Eighteen",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.ktKdsvMUOsYCxfTx_FuE-gHaE6?w=259&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 19,
        "location": "Antipolo",
        "restaurant_name": "Restaurant Nineteen",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.nab44Acdj2V5NxEi-qDjFQHaEr?w=288&h=182&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 20,
        "location": "Batangas",
        "restaurant_name": "Restaurant Twenty",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.NaMf-h29-XiZH8uPQEfXPAHaFW?w=257&h=186&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 21,
        "location": "Quezon City",
        "restaurant_name": "Restaurant Twenty-One",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.XYSwD92_1dMxg6LvTZxKtAHaE8?w=280&h=186&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 22,
        "location": "Pasig",
        "restaurant_name": "Restaurant Twenty-Two",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIF.p42P6Jgnrd3Ht1FfKtJtjg?w=205&h=204&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 23,
        "location": "Manila",
        "restaurant_name": "Restaurant Twenty-Three",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIF.QjffbnDnWEWI4EhO6EBonw?w=286&h=191&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 24,
        "location": "Laguna",
        "restaurant_name": "Restaurant Twenty-Four",
        "status": "Open",
        "image_url": "https://th.bing.com/th?id=OIF.Yk%2bskUYk2QcbJ%2bTO5UXSZw&w=308&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 25,
        "location": "Quezon City",
        "restaurant_name": "Restaurant Twenty-Five",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIF.Z3PazMaTjmnVFScDX71kMg?w=260&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 26,
        "location": "Makati",
        "restaurant_name": "Restaurant Twenty-Six",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIF.1H3u2gGYnemdeT9zHfwNUw?w=280&h=182&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 27,
        "location": "Cebu",
        "restaurant_name": "Restaurant Twenty-Seven",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIF.lFBYBC0BrGTBHNjiBYpuBw?w=121&h=182&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 28,
        "location": "Davao",
        "restaurant_name": "Restaurant Twenty-Eight",
        "status": "Open",
        "image_url": "https://th.bing.com/th?id=OIF.ALGls%2fy78vp8Oco%2bNZx9yg&w=241&h=187&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 29,
        "location": "Pasig",
        "restaurant_name": "Restaurant Twenty-Nine",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIF.Y1zm9hF5xb9c2m8zm29r5w?w=278&h=189&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 30,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Thirty",
        "status": "Open",
        "image_url": "https://th.bing.com/th?id=OIF.rvIn8hIKofDGsV%2fLjlLh2Q&w=247&h=189&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 31,
        "location": "Taguig",
        "restaurant_name": "Restaurant Thirty-One",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIF.WTFNfNhuDyrGcdk3CJbSzQ?w=235&h=184&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 32,
        "location": "Alabang",
        "restaurant_name": "Restaurant Thirty-Two",
        "status": "Open",
        "image_url": "https://th.bing.com/th?id=OIF.7se2thPr9MD%2bWj7MmkWi8A&w=228&h=190&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 33,
        "location": "Makati",
        "restaurant_name": "Restaurant Thirty-Three",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.pUHyxDw89hfkIv3jD6GxgwHaDv?w=328&h=176&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 34,
        "location": "Quezon City",
        "restaurant_name": "Restaurant Thirty-Four",
        "status": "Open",
        "image_url": "http://ts1.mm.bing.net/th?id=OIP.OcyDNImucTxI8K3lwZ_nlAHaFM&pid=15.1"
    },
    {
        "id": 35,
        "location": "Pasig",
        "restaurant_name": "Restaurant Thirty-Five",
        "status": "Closed",
        "image_url": "http://ts4.mm.bing.net/th?id=OIP.Rz8K-8bv6shCx7ECkBH4_wHaE0&pid=15.1"
    },
    {
        "id": 36,
        "location": "Las Piñas",
        "restaurant_name": "Restaurant Thirty-Six",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.VUBnzu2ozNaoieiBcuRP9wHaE_?w=259&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 37,
        "location": "Muntinlupa",
        "restaurant_name": "Restaurant Thirty-Seven",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.J96Eq0L7xcXj7mwkH9TiewHaEK?w=311&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 38,
        "location": "Pasay",
        "restaurant_name": "Restaurant Thirty-Eight",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.r-LZKef20qTHaMbUu7rCXwHaE8?w=301&h=200&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 39,
        "location": "Cavite",
        "restaurant_name": "Restaurant Thirty-Nine",
        "status": "Closed",
        "image_url": "https://th.bing.com/th?id=OIF.w%2by9T%2fyQZdTkedNVSlBcGQ&rs=1&pid=ImgDetMain"
    },
    {
        "id": 40,
        "location": "Parañaque",
        "restaurant_name": "Restaurant Forty",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.VOs5Ez6o0elAbgqvzglX9wHaFO?w=242&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 41,
        "location": "Batangas",
        "restaurant_name": "Restaurant Forty-One",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.7fvmnhK104QWUMHHTHP9pAHaE7?w=250&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 42,
        "location": "Taguig",
        "restaurant_name": "Restaurant Forty-Two",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.-lyObdkp8zo-p1h7OyOUdAHaE8?w=284&h=189&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 43,
        "location": "Quezon City",
        "restaurant_name": "Restaurant Forty-Three",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.AIfaApTjXkZYO23toY6BwwHaEK?w=303&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 44,
        "location": "Makati",
        "restaurant_name": "Restaurant Forty-Four",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.3-T04iChHzc3YRQR9F_GhwHaGj?w=226&h=200&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 45,
        "location": "Pasig",
        "restaurant_name": "Restaurant Forty-Five",
        "status": "Closed",
        "image_url": "http://ts1.mm.bing.net/th?id=OIP.OcyDNImucTxI8K3lwZ_nlAHaFM&pid=15.1"
    },
    {
        "id": 46,
        "location": "Manila",
        "restaurant_name": "Restaurant Forty-Six",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.eT2qT8agCAN51Mvp-YVvIQHaGR?w=198&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 47,
        "location": "Cebu",
        "restaurant_name": "Restaurant Forty-Seven",
        "status": "Closed",
        "image_url": "https://th.bing.com/th?id=OIF.vOlOTfyQtIziF1zk3k%2b4wA&w=168&h=220&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 48,
        "location": "Davao",
        "restaurant_name": "Restaurant Forty-Eight",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.0PNUE5cadALtOM1x2zY68wHaE6?w=296&h=196&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 49,
        "location": "Baguio",
        "restaurant_name": "Restaurant Forty-Nine",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.BYWHwvA4y4-Nrxp6v0BVQQHaE8?w=279&h=186&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    },
    {
        "id": 50,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Fifty",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.jaBHiz3VD_IRaoVIiNhxsAHaEm?w=248&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"
    }
]




@app.route('/')
def hello_world():
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)