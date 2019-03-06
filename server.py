from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/profile')
def profile():
    return jsonify({
        'data': [
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile001.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile002.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile003.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile010.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile011.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile012.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile301.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile302.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile311.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile321.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile322.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile998.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/profile999.json'},
        ]
    })


@app.route('/product')
def product():
    return jsonify({
        'data': [
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product001.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product002.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product003.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product010.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product011.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product101.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product102.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product111.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product112.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product121.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product122.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product999.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product301.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product321.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/product322.json'},
        ]
    })


@app.route('/offer')
def offer():
    return jsonify({
        'data': [
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00001.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00002.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00003.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00010.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00011.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00020.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00021.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00030.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00031.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00040.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00101.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00102.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00111.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00112.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00121.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00122.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00301.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00302.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00321.json'},
            {'url': 'https://catalog.openprocurement.org.ua/catalog/offer00322.json'},
        ]
    })


if __name__ == '__main__':
    app.run(host='localhost', port=9000)
