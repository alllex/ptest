#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-07

# -------------------------------------------------------
#                     Addition Tests
# -------------------------------------------------------

package perl::tests::addition;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK %EXPORT_TAGS);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test &params);
@EXPORT_OK   = qw(test params);

sub test { $_[0] + $_[1] }
sub params {
    get_data('AdditionOfInt');
}

1;