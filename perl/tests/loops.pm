#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-18

# -------------------------------------------------------
#                Loop For C-Style Tests
# -------------------------------------------------------

package perl::tests::loop_for_c;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_loop_for_c);
@EXPORT_OK   = qw(test_loop_for_c);

sub test_loop_for_c { 
    my $b = !! 0;
    for (my $i = 0; $i < $_[0]; $i++) {
        $b = ! $b;
    }
    1;
}

package perl::tests::loop_for_range;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_loop_for_range);
@EXPORT_OK   = qw(test_loop_for_range);

sub test_loop_for_range { 
    my $b = !! 0;
    for (0..$_[0]) {
        $b = ! $b;
    }
    1;
}

package perl::tests::loop_while;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_loop_while);
@EXPORT_OK   = qw(test_loop_while);

sub test_loop_while { 
    my $b = !! 0;
    my $i = 0;
    while ($i < $_[0]) {
        $i++;
        $b = ! $b;
    }
    1;
}

package perl::tests::loop_foreach;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_loop_foreach);
@EXPORT_OK   = qw(test_loop_foreach);

sub test_loop_foreach { 
    my $b = !! 0;
    foreach my $i (0..$_[0]) {
        $b = ! $b;
    }
    1;
}

1;