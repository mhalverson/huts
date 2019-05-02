import base64
import hashlib


def encode_hut(hut):
    starting_str = '{}{}'.format(hut.name, hut.region)
    sha = hashlib.sha1(starting_str.encode('utf-8')).hexdigest().encode('utf-8')
    b64 = base64.b64encode(sha)[:5]
    return b64.decode('utf-8')

def to_encoded_hut_dict(huts):
    result = {}
    for h in huts:
        result[encode_hut(h)] = {
            'name': h.name,
            'place': h.place,
            'region': h.region,
            'island': h.island,
            'lat': h.lat,
            'lng': h.lng,
            'url': h.url,
        }
    return result


if __name__ == '__main__':
    import json
    from pprint import pprint
    from huts.hut import all_huts
    from huts.merged import filter_known_region_known_place

    huts = filter_known_region_known_place(all_huts())
    # print(encode_hut(huts[0]))
    with open('encoded_hut_dict.js', 'w') as f:
        f.write('var encodedHutDict = ')
        f.write(json.dumps(to_encoded_hut_dict(huts)))
        f.write(';\n')
        f.write('''
            async function encodeHut( str ) {
              const buffer = new TextEncoder( 'utf-8' ).encode( str );
              const digest = await crypto.subtle.digest('SHA-1', buffer);
              // Convert digest to hex string
              const hexStr = Array.from(new Uint8Array(digest)).map( x => x.toString(16).padStart(2,'0') ).join('');
              const b64Str = btoa(hexStr);
              return b64Str.slice(0, 5);
            }

            function lookupHut( encodedHut ) {
              return encodedHutDict[encodedHut];
            }
        ''')
