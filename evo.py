import string
import random

model_genes = ['1','2','3','4','a','b','c','d']
strand = len(model_genes)/2

def female_code(size, chars=string.digits):
	return list(''.join(random.choice(chars) for _ in range(size)))

def male_code(size, chars=string.ascii_lowercase):
	return list(''.join(random.choice(chars) for _ in range(size)))

class Lifeform(object):
	def __init__(self, female_, male_):
		self.female_genes = female_
		self.male_genes = male_

	def dna(self):
		return self.female_genes + self.male_genes

	def generation(self,num):
		self.branch = num
		return self.branch

def breed(male, female): 
	gene_length = len(model_genes)
	gene_split = gene_length / 2
	x_model = model_genes[:gene_split]
	y_model = model_genes[gene_split:]

	organism_1 = male
	organism_2 = female

	#male dna extract
	o1_x_dna = organism_1.dna()[:gene_split]
	o1_y_dna = organism_1.dna()[gene_split:]

	#female dna extract
	o2_x_dna = organism_2.dna()[:gene_split]
	o2_y_dna = organism_2.dna()[gene_split:]
	
	def dna_match(model_dna, organism_dna):
		gene_test = set(model_dna) & set(organism_dna)
		return list(gene_test)

	def get_inheritance():
		x_traits = dna_match(x_model, o1_x_dna) + dna_match(x_model, o2_x_dna)
		y_traits = dna_match(y_model, o1_y_dna) + dna_match(y_model, o2_y_dna)
	
		offspring_x_traits = sorted(list(set(x_traits)))
		offspring_y_traits = sorted(list(set(y_traits)))

		print "Desired DNA:",model_genes
		print "Father's DNA:",sorted(organism_1.dna())
		print "Mother's DNA:",sorted(organism_2.dna())
		print "Child's inherited traits",offspring_x_traits,offspring_y_traits
		return offspring_x_traits,offspring_y_traits

	def produce_child(xi,yi): #takes arrays of inherited DNA
		x_needed = gene_split-len(xi)
		y_needed = gene_split-len(yi)

		child = Lifeform(female_code(x_needed),male_code(y_needed))
		inherited_genes = sorted(xi+yi)
		child_dna = sorted(inherited_genes + child.dna())


		print "Child's DNA:",child_dna


	x_heredity,y_heredity = get_inheritance()
	return produce_child(x_heredity,y_heredity)

breed(Lifeform(female_code(strand),male_code(strand)),
		Lifeform(female_code(strand),male_code(strand)))
