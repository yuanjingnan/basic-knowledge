from ete3 import NCBITaxa

# Initialize NCBITaxa object
ncbi = NCBITaxa()

# Function to parse Kraken2 report and extract TaxIDs
def parse_kraken2_report(file_path):
    taxid_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            fields = line.strip().split("\t")
            if len(fields) > 4:
                taxid = fields[4]  # TaxID is in the 5th column
                taxid_set.add(int(taxid))  # Add to the set to avoid duplicates
    return list(taxid_set)

# Function to build a tree from TaxIDs
def build_taxonomic_tree(taxids):
    # Fetch the taxonomic tree based on the TaxIDs
    tree = ncbi.get_topology(taxids)
    return tree

# Function to visualize the tree
def show_tree(tree):
    tree.show()

# Optionally, you can export the tree to Newick or an image
def save_tree(tree, output_file):
    tree.write(format=1, outfile=output_file)
    tree.render(output_file.replace(".nwk", ".png"), w=183, units="mm")

# Main workflow
#kraken2_report_file = "/Users/yuanjingnan/Desktop/daily/20241023/kraken2_report.all.tsv"  # Update this path
#taxids = parse_kraken2_report(kraken2_report_file)
#print(f"Found {len(taxids)} unique TaxIDs.")

#tree = build_taxonomic_tree(taxids)

# Show the tree interactively
#show_tree(tree)

# Optionally, save the tree to a Newick file and an image
#save_tree(tree, "kraken2_taxonomic_tree.nwk")