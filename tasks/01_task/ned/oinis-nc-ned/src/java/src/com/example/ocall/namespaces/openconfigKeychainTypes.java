/*
 * BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE
 * This file has been auto-generated by the confdc compiler.
 * Source: ../load-dir/openconfig-keychain-types.fxs
 * BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE
 */

package com.example.ocall.namespaces;

import com.tailf.conf.ConfNamespace;

/** Autogenerated namespace class for YANG module openconfig-keychain-types.yang */
public class openconfigKeychainTypes extends ConfNamespace {
    public static final int hash = 727414280;
    public int hash() {
        return openconfigKeychainTypes.hash;
    }

    public static final String id = "_oinis-nc-ned-nc-1.0:oinis-nc-ned-nc-1.0#http://openconfig.net/yang/oc-keychain-types";
    public String id() {
        return openconfigKeychainTypes.id;
    }

    public static final String uri = "_oinis-nc-ned-nc-1.0:oinis-nc-ned-nc-1.0#http://openconfig.net/yang/oc-keychain-types";
    public String uri() {
        return openconfigKeychainTypes.uri;
    }

    public String xmlUri() {
        return ConfNamespace.truncateToXMLUri(openconfigKeychainTypes.uri);
    }

    public static final String prefix = "oc-keychain-types";
    public String prefix() {
        return openconfigKeychainTypes.prefix;
    }

    public openconfigKeychainTypes() {}

    public static int stringToHash(String str) {
        return ConfNamespace.stringToHash(str);
    }

    public static String hashToString(int hash) {
        return ConfNamespace.hashToString(hash);
    }

    public static final int    _AUTH_TYPE = 1660103911;
    public static final String _AUTH_TYPE_ = "AUTH_TYPE";
    public static final int    _HMAC_SHA_256 = 1562330574;
    public static final String _HMAC_SHA_256_ = "HMAC_SHA_256";
    public static final int    _KEYCHAIN = 1155486059;
    public static final String _KEYCHAIN_ = "KEYCHAIN";
    public static final int    _MD5 = 959247075;
    public static final String _MD5_ = "MD5";
    public static final int    _HMAC_MD5 = 311208841;
    public static final String _HMAC_MD5_ = "HMAC_MD5";
    public static final int    _HMAC_SHA_1_20 = 722257776;
    public static final String _HMAC_SHA_1_20_ = "HMAC_SHA_1_20";
    public static final int    _HMAC_SHA_1_96 = 1830445351;
    public static final String _HMAC_SHA_1_96_ = "HMAC_SHA_1_96";
    public static final int    _HMAC_SHA_1_12 = 1073873167;
    public static final String _HMAC_SHA_1_12_ = "HMAC_SHA_1_12";
    public static final int    _SIMPLE_KEY = 2039954345;
    public static final String _SIMPLE_KEY_ = "SIMPLE_KEY";
    public static final int    _AES_28_CMAC_96 = 813559548;
    public static final String _AES_28_CMAC_96_ = "AES_28_CMAC_96";
    public static final int    _CRYPTO_NONE = 773527962;
    public static final String _CRYPTO_NONE_ = "CRYPTO_NONE";
    public static final int    _SHA_1 = 133308218;
    public static final String _SHA_1_ = "SHA_1";
    public static final int    _HMAC_SHA_1 = 512846102;
    public static final String _HMAC_SHA_1_ = "HMAC_SHA_1";
    public static final int    _CRYPTO_TYPE = 1997504641;
    public static final String _CRYPTO_TYPE_ = "CRYPTO_TYPE";
}
