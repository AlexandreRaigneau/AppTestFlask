#!/usr/bin/perl
use strict;
use warnings;

print("salut\n");

# Un tableau avec des valeurs dupliquées :
my @t = qw(hello toto hello vous);

# Déclaration d'une table de hachage :
my %h;

# On prend la tranche de %h dont les clefs
# sont les valeurs du tableau @t
# et on leur associe la valeur undef
@h{@t} = ();

# Les clefs de %h sont donc constituées des
# valeurs de @t, et on est sûr de ne les
# retrouver qu'une seule fois :
@t = keys %h;

foreach my $key (@t){
    print("$key\n");
};