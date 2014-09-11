#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-11

use strict;
use perl::tests::addition;

# -------------------------------------------------------
#                     Benchmark utils
# -------------------------------------------------------


sub benchmark {
    my ($test, $params) = @_;
    my @data = $params->();
    for my $param (@data) {
        print $test->(@$param), "\n";
    }
}

sub mk_bunch ($) {
    no strict 'refs';
    sub mk_sub { \&{"perl\:\:tests\:\:$_[0]\:\:$_[1]"} }
    (
        mk_sub($_[0], 'test'), 
        mk_sub($_[0], 'params')
    );
}

benchmark(mk_bunch("addition"));