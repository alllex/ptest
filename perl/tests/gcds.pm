#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-18

# -------------------------------------------------------
#                      GCD Tests
# -------------------------------------------------------

package perl::tests::gcd_by_rec;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_gcd_by_rec);
@EXPORT_OK   = qw(test_gcd_by_rec);

sub test_gcd_by_rec { 
    $_[1] ? test_gcd_by_rec($_[1], $_[0] % $_[1]) : $_[0] 
}

package perl::tests::gcd_by_loop;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_gcd_by_loop);
@EXPORT_OK   = qw(test_gcd_by_loop);

sub test_gcd_by_loop { 
    my ($a, $b) = @_;
    while ($b != 0) {
        ($a, $b) = ($b, $a % $b);
    }
    $a;
}

1;