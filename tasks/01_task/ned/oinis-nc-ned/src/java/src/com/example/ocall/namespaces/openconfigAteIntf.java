/*
 * BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE
 * This file has been auto-generated by the confdc compiler.
 * Source: ../load-dir/openconfig-ate-intf.fxs
 * BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE
 */

package com.example.ocall.namespaces;

import com.tailf.conf.ConfNamespace;

/** Autogenerated namespace class for YANG module openconfig-ate-intf.yang */
public class openconfigAteIntf extends ConfNamespace {
    public static final int hash = 1088292171;
    public int hash() {
        return openconfigAteIntf.hash;
    }

    public static final String id = "_oinis-nc-ned-nc-1.0:oinis-nc-ned-nc-1.0#http://openconfig.net/yang/ate-intf";
    public String id() {
        return openconfigAteIntf.id;
    }

    public static final String uri = "_oinis-nc-ned-nc-1.0:oinis-nc-ned-nc-1.0#http://openconfig.net/yang/ate-intf";
    public String uri() {
        return openconfigAteIntf.uri;
    }

    public String xmlUri() {
        return ConfNamespace.truncateToXMLUri(openconfigAteIntf.uri);
    }

    public static final String prefix = "oc-atei";
    public String prefix() {
        return openconfigAteIntf.prefix;
    }

    public openconfigAteIntf() {}

    public static int stringToHash(String str) {
        return ConfNamespace.stringToHash(str);
    }

    public static String hashToString(int hash) {
        return ConfNamespace.hashToString(hash);
    }

    public static final int    _out_rate = 268343224;
    public static final String _out_rate_ = "out-rate";
    public static final int    _in_rate = 1162687589;
    public static final String _in_rate_ = "in-rate";
}
