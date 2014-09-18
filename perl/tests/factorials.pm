#!/bin/perl

# Project: ptest
# Module:  perl
# Author:  alllex
# Date  :  2014-09-18

# -------------------------------------------------------
#                   Factorial Tests
# -------------------------------------------------------

package perl::tests::fact_by_mathlib;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_fact_by_mathlib);
@EXPORT_OK   = qw(test_fact_by_mathlib);

sub test_fact_by_mathlib { 
    use Math::BigInt lib => 'GMP';
    $b = Math::BigInt->new($_[0]);
    $b->bfac();
}

package perl::tests::fact_by_rec;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_fact_by_rec);
@EXPORT_OK   = qw(test_fact_by_rec);

sub test_fact_by_rec { 
    $_[0] ? $_[0] * test_fact_by_rec($_[0] - 1) : 1
}

package perl::tests::fact_by_loop;

use strict;
use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

use perl::tests::test;

$VERSION     = 1.00;
@ISA         = qw(Exporter);
@EXPORT      = qw(&test_fact_by_loop);
@EXPORT_OK   = qw(test_fact_by_loop);

sub test_fact_by_loop { 
    my $total = my $n = shift;
    while ($n > 1) {
        $total *= ($n-- - 1);
    }
    $total;
}

1;