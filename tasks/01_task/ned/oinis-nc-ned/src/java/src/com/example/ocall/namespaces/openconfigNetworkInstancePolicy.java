/*
 * BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE
 * This file has been auto-generated by the confdc compiler.
 * Source: ../load-dir/openconfig-network-instance-policy.fxs
 * BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE BEWARE
 */

package com.example.ocall.namespaces;

import com.tailf.conf.ConfNamespace;

/** Autogenerated namespace class for YANG module openconfig-network-instance-policy.yang */
public class openconfigNetworkInstancePolicy extends ConfNamespace {
    public static final int hash = 1636986811;
    public int hash() {
        return openconfigNetworkInstancePolicy.hash;
    }

    public static final String id = "_oinis-nc-ned-nc-1.0:oinis-nc-ned-nc-1.0#http://openconfig.net/yang/network-instance/policy";
    public String id() {
        return openconfigNetworkInstancePolicy.id;
    }

    public static final String uri = "_oinis-nc-ned-nc-1.0:oinis-nc-ned-nc-1.0#http://openconfig.net/yang/network-instance/policy";
    public String uri() {
        return openconfigNetworkInstancePolicy.uri;
    }

    public String xmlUri() {
        return ConfNamespace.truncateToXMLUri(openconfigNetworkInstancePolicy.uri);
    }

    public static final String prefix = "oc-ni-pol";
    public String prefix() {
        return openconfigNetworkInstancePolicy.prefix;
    }

    public openconfigNetworkInstancePolicy() {}

    public static int stringToHash(String str) {
        return ConfNamespace.stringToHash(str);
    }

    public static String hashToString(int hash) {
        return ConfNamespace.hashToString(hash);
    }

    public static final int    _protocol_name = 684080917;
    public static final String _protocol_name_ = "protocol-name";
    public static final int    _protocol_identifier = 1431250581;
    public static final String _protocol_identifier_ = "protocol-identifier";
    public static final int    _state = 630973766;
    public static final String _state_ = "state";
    public static final int    _config = 2105663071;
    public static final String _config_ = "config";
    public static final int    _match_protocol_instance = 1433286145;
    public static final String _match_protocol_instance_ = "match-protocol-instance";
}
