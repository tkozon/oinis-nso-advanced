/*
 * BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE
 * This file has been auto-generated by the confdc compiler.
 * Source: ../load-dir/openconfig-alarms.fxs
 * BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE
 */

package com.example.ocall.namespaces;

import com.tailf.conf.ConfNamespace;

/** Autogenerated namespace class for YANG module openconfig-alarms.yang */
public class openconfigAlarms extends ConfNamespace {
    public static final int hash = 805894450;
    public int hash() {
        return openconfigAlarms.hash;
    }

    public static final String id = "_oinis-nc-ned-nc-1.0:oinis-nc-ned-nc-1.0#http://openconfig.net/yang/alarms";
    public String id() {
        return openconfigAlarms.id;
    }

    public static final String uri = "_oinis-nc-ned-nc-1.0:oinis-nc-ned-nc-1.0#http://openconfig.net/yang/alarms";
    public String uri() {
        return openconfigAlarms.uri;
    }

    public String xmlUri() {
        return ConfNamespace.truncateToXMLUri(openconfigAlarms.uri);
    }

    public static final String prefix = "oc-alarms";
    public String prefix() {
        return openconfigAlarms.prefix;
    }

    public openconfigAlarms() {}

    public static int stringToHash(String str) {
        return ConfNamespace.stringToHash(str);
    }

    public static String hashToString(int hash) {
        return ConfNamespace.hashToString(hash);
    }

    public static final int    _equipment_failure = 1499913034;
    public static final String _equipment_failure_ = "equipment-failure";
    public static final int    _equipment_mismatch = 1812222;
    public static final String _equipment_mismatch_ = "equipment-mismatch";
}
