#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-11

# -------------------------------------------------------
#                     Addition Tests
# -------------------------------------------------------

package perl::tests::test;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK %EXPORT_TAGS);

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&get_data &subject &get_prefs);
@EXPORT_OK   = qw(get_data subject get_prefs);

sub subject {
    return 'perl-' . $^V;
}

sub get_prefs {
    my $file_name = "data/gen/prefs.data";
    open (my $file, "<", $file_name) || die "Can't read file: $!";
    map { $_ =~ /(\d+)/ } <$file>;
}

sub get_data ($) {
    my $test_name = shift;
    my $file_name = "data/gen/$test_name.data";
    open (my $file, "<", $file_name) || die "Can't read file: $!";
    map [ split ], <$file>;
}

1;