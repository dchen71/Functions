class CreateReviews < ActiveRecord::Migration
  def change
    create_table :reviews do |t|
	  t.string :author
	  t.string :comment
	  t.references :book

      t.timestamps null: false
    end
  end
end
